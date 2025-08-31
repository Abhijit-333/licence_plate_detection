
from google.cloud import vision
import io

def detect_text(path):
    #useGoogle Vision API 
    client = vision.ImageAnnotatorClient()

    with io.open(path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    if response.error.message:
        raise Exception(f"Google Vision API error: {response.error.message}")

    if texts:
        return texts[0].description.strip()
    else:
        return None

