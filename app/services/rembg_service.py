from rembg import remove, new_session
from PIL import Image
from io import BytesIO

# lightweight session (recommended)
session = new_session("u2netp")  # u2netp = smaller model, less RAM

def remove_background(image_bytes: bytes) -> bytes:
    input_image = Image.open(BytesIO(image_bytes)).convert("RGBA")

    # Resize to reduce RAM (max 1024px)
    max_size = 1024
    w, h = input_image.size
    if max(w, h) > max_size:
        ratio = max_size / float(max(w, h))
        input_image = input_image.resize((int(w * ratio), int(h * ratio)))

    output = remove(input_image, session=session)

    out_buffer = BytesIO()
    output.save(out_buffer, format="PNG")
    return out_buffer.getvalue()
