import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")
    DB_USER = os.getenv("DB_USER", "postgres")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "5432")
    DB_NAME = os.getenv("DB_NAME", "master_data_db")
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}"
        f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = os.getenv("SQLALCHEMY_ECHO", "false").lower() in ("1", "true", "yes")

    # API versioning: all routes are mounted under this prefix (e.g. /api/v1/health)
    API_V1_PREFIX = os.getenv("API_V1_PREFIX", "/api/v1")

    # JWT validation (same secret as auth service that issues tokens)
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "change-me-in-production")
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
    JWT_ACCESS_TOKEN_EXPIRES = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES", "3600"))  # seconds

    # Request/response logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
    LOG_REQUEST_BODY_MAX_LENGTH = int(os.getenv("LOG_REQUEST_BODY_MAX_LENGTH", "2048"))
    LOG_RESPONSE_BODY_MAX_LENGTH = int(os.getenv("LOG_RESPONSE_BODY_MAX_LENGTH", "2048"))
