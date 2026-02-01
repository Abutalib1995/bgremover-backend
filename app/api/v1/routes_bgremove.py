import uuid
from pathlib import Path
from fastapi import APIRouter, UploadFile, File, Request
from fastapi.responses import JSONResponse
import aiofiles

from app.core.config import UPLOAD_DIR, OUTPUT_DIR
from app.utils.file_validator import validate_upload, validate_size
from app.services.rembg_service import remove_background

router = APIRouter()

@router.post("/bg-remove")
async def bg_remove(request: Request, file: UploadFile = File(...)):
    validate_upload(file)

    # Read bytes
    content = await file.read()
    validate_size(len(content))

    # Prepare dirs
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    job_id = str(uuid.uuid4())

    # Save original (optional but good for debugging)
    upload_path = UPLOAD_DIR / f"{job_id}_{file.filename}"
    async with aiofiles.open(upload_path, "wb") as f:
        await f.write(content)

    # Remove background
    out_bytes = remove_background(content)

    # Save output PNG
    output_filename = f"{job_id}.png"
    output_path = OUTPUT_DIR / output_filename
    async with aiofiles.open(output_path, "wb") as f:
        await f.write(out_bytes)

    # Public output URL
    base_url = str(request.base_url).rstrip("/")
    output_url = f"{base_url}/files/outputs/{output_filename}"

    return JSONResponse(
        {
            "status": "success",
            "job_id": job_id,
            "output_url": output_url
        }
    )
