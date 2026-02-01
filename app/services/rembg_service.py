from rembg import remove
from PIL import Image
from io import BytesIO

def remove_background(image_bytes: bytes) -> bytes:
    """
    Takes image bytes (jpg/png/webp) and returns PNG bytes (transparent bg).
    """
    input_image = Image.open(BytesIO(image_bytes)).convert("RGBA")
    output = remove(input_image)

    out_buffer = BytesIO()
    output.save(out_buffer, format="PNG")
    return out_buffer.getvalue()
