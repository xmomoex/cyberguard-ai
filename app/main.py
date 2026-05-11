from fastapi import FastAPI

from app.core.database import Base, engine
from app.models import user, scan

from app.api.routes_auth import router as auth_router
from app.api.routes_users import router as users_router
from app.api.routes_scan import router as scan_router
from app.api.routes_web import router as web_router

from fastapi.openapi.utils import get_openapi

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request


# Crear tablas en DB
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="CyberGuard AI",
    description="AI-powered malicious URL detector",
    version="1.0.0"
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


# -----------------------------
# ROUTERS
# -----------------------------
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(scan_router)
app.include_router(web_router)




# -----------------------------
# SWAGGER AUTH CONFIG (JWT)
# -----------------------------
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="CyberGuard AI",
        version="1.0.0",
        description="AI-powered malicious URL detector",
        routes=app.routes,
    )

    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }

    for path in openapi_schema["paths"]:
        for method in openapi_schema["paths"][path]:
            openapi_schema["paths"][path][method]["security"] = [
                {"BearerAuth": []}
            ]

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

