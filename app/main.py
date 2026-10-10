import os
import base64
from fastapi import FastAPI, Request
from fastapi.responses import Response
from starlette.middleware.base import BaseHTTPMiddleware

from app.database import Base, engine
from app.routes import auth, products

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Portfolio Auth API",
    description="API REST avec authentification JWT — Projet 1",
    version="1.0.0",
)


class BasicAuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Exclure les routes de documentation (avec ou sans préfixe /api)
        excluded_suffixes = ["/docs", "/openapi.json", "/redoc", "/docs/oauth2-redirect"]
        if any(request.url.path.endswith(suffix) for suffix in excluded_suffixes):
            return await call_next(request)

        valid_username = os.getenv("BASIC_AUTH_USERNAME", "admin")
        valid_password = os.getenv("BASIC_AUTH_PASSWORD", "password")

        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Basic "):
            return Response(
                content="Accès refusé. Identifiants requis.",
                status_code=401,
                headers={"WWW-Authenticate": "Basic"},
            )

        try:
            encoded_credentials = auth_header.split(" ")[1]
            decoded_credentials = base64.b64decode(encoded_credentials).decode("utf-8")
            username, password = decoded_credentials.split(":", 1)

            if username == valid_username and password == valid_password:
                return await call_next(request)
            else:
                raise ValueError("Identifiants incorrects")
        except Exception:
            return Response(
                content="Identifiants incorrects.",
                status_code=401,
                headers={"WWW-Authenticate": "Basic"},
            )


app.add_middleware(BasicAuthMiddleware)

app.include_router(auth.router)
app.include_router(products.router)


@app.get("/")
def root():
    return {"message": "API en ligne"}


@app.get("/health")
def health_check():
    return {"status": "ok", "message": "API opérationnelle"}
