from fastapi import HTTPException, UploadFile
from app.core.config import MAX_UPLOAD_MB, ALLOWED_MIME

def validate_upload(file: UploadFile):
    if not file:
        raise HTTPException(status_code=400, detail="No file provided")

    if file.content_type not in ALLOWED_MIME:
        raise HTTPException(status_code=415, detail="Unsupported file type")

def validate_size(size_bytes: int):
    max_bytes = MAX_UPLOAD_MB * 1024 * 1024
    if size_bytes > max_bytes:
        raise HTTPException(status_code=413, detail=f"File too large. Max {MAX_UPLOAD_MB}MB")
