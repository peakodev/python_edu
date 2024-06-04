from fastapi.middleware.cors import CORSMiddleware

from src.conf.config import settings


def apply_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
