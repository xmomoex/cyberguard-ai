from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/")
def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@router.get("/login")
def login_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="login.html"
    )


@router.get("/register")
def register_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="register.html"
    )


@router.get("/dashboard")
def dashboard_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="dashboard.html"
    )


@router.get("/scans")
def scans_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="scans.html"
    )