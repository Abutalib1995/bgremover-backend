FROM python:3.11-slim

WORKDIR /app

# Install system deps (needed by rembg/onnx + image processing)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Ensure storage folders exist (good for first run)
RUN mkdir -p /app/storage/uploads /app/storage/outputs

ENV PORT=8000
EXPOSE 8000

# Start FastAPI
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT}"]
