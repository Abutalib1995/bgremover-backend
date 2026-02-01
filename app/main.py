from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.core.config import CORS_ORIGINS, OUTPUT_DIR
from app.api.v1.routes_bgremove import router as bg_router

app = FastAPI(title="Background Remover API", version="1.0.0")

# CORS (static site support)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[o.strip() for o in CORS_ORIGINS] if CORS_ORIGINS else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(bg_router, prefix="/api/v1", tags=["Background Removal"])

# Serve output files publicly
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
app.mount("/files/outputs", StaticFiles(directory=str(OUTPUT_DIR)), name="outputs")
