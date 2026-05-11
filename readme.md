# 🛡️ CyberGuard AI

## 📌 Descripción del proyecto

CyberGuard AI es un sistema inteligente de ciberseguridad basado en FastAPI que permite analizar URLs en tiempo real para detectar posibles amenazas como phishing, malware o sitios sospechosos.

El sistema combina:

* 🔍 Análisis heurístico de URLs
* 🧠 Explicaciones generadas por inteligencia artificial
* 👤 Autenticación de usuarios con JWT
* 📊 Historial de análisis por usuario
* 🐳 Despliegue completo con Docker

El objetivo del proyecto es simular una herramienta real de ciberseguridad tipo VirusTotal pero enfocada en aprendizaje y detección básica asistida por IA.

---

# ⚙️ Tecnologías utilizadas

* FastAPI
* PostgreSQL
* SQLAlchemy
* JWT Authentication
* Docker & Docker Compose
* HTML + CSS + JavaScript (frontend simple)
* OpenAI API (opcional para explicación IA)

---

# 🚀 Instrucciones de instalación

## 1. Clonar el repositorio

```bash
git clone https://github.com/xmomoex/cyberguard-ai.git
cd cyberguard-ai
```

---

## 2. Configurar variables de entorno

Crear archivo `.env`:

```env
DATABASE_URL=postgresql://user:password@db:5432/cyberguard
SECRET_KEY=supersecretkey
OPENAI_API_KEY=tu_api_key (opcional)
```

---

## 3. Levantar el sistema con Docker

```bash
docker-compose up --build
```

Esto levantará:

* Backend FastAPI
* Base de datos PostgreSQL

---

## 4. Acceder a la aplicación

* API: [http://localhost:8000](http://localhost:8000)
* Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
* Frontend: [http://localhost:8000/](http://localhost:8000/)

---

# 📡 Uso de la API

## 🔐 Autenticación

### Registro

```http
POST /auth/register
```

Body:

```json
{
  "username": "test",
  "email": "test@email.com",
  "password": "1234"
}
```

---

### Login

```http
POST /auth/login
```

Body:

```json
{
  "email": "test@email.com",
  "password": "1234"
}
```

Respuesta:

```json
{
  "access_token": "jwt_token",
  "token_type": "bearer"
}
```

---

## 🧪 Escanear URL

```http
POST /scan/url
```

Headers:

```http
Authorization: Bearer <token>
```

Body:

```json
{
  "url": "http://example.com"
}
```

Respuesta:

```json
{
  "url": "http://example.com",
  "risk": "HIGH",
  "score": 85,
  "reasons": ["suspicious domain"],
  "ai_explanation": "Explicación generada por IA..."
}
```

---

## 📜 Historial de scans

```http
GET /scan/history
```

Headers:

```http
Authorization: Bearer <token>
```

---

## 🔍 Obtener scan específico

```http
GET /scan/{id}
```

---

## ❌ Eliminar scan

```http
DELETE /scan/{id}
```

---

# 🐳 Configuración Docker

## docker-compose.yml

El sistema incluye:

* Backend FastAPI
* PostgreSQL database

### Levantar todo:

```bash
docker-compose up --build
```

### Detener:

```bash
docker-compose down
```

---

# 📚 Documentación API (Swagger)

El proyecto incluye documentación automática:

👉 [http://localhost:8000/docs](http://localhost:8000/docs)

Características:

* Prueba de endpoints en tiempo real
* Autenticación JWT integrada
* Esquemas automáticos con Pydantic

---

# 🧠 Arquitectura del sistema

```
Frontend (HTML/JS)
        ↓
FastAPI Backend
        ↓
Servicios:
- Scanner URL
- IA (OpenAI / lógica local)
- Auth JWT
        ↓
PostgreSQL Database
```

---

# 🔥 Funcionalidades principales

* ✔ Registro y login de usuarios
* ✔ Autenticación con JWT
* ✔ Análisis de URLs sospechosas
* ✔ Clasificación de riesgo (LOW / MEDIUM / HIGH)
* ✔ Explicación generada por IA
* ✔ Historial personalizado por usuario
* ✔ API REST completa
* ✔ Dockerizado completamente


