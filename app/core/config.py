import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

UPLOAD_DIR = Path(os.getenv("UPLOAD_DIR", BASE_DIR / "storage" / "uploads"))
OUTPUT_DIR = Path(os.getenv("OUTPUT_DIR", BASE_DIR / "storage" / "outputs"))

MAX_UPLOAD_MB = int(os.getenv("MAX_UPLOAD_MB", "10"))
ALLOWED_MIME = {"image/jpeg", "image/png", "image/webp"}

CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*").split(",")
