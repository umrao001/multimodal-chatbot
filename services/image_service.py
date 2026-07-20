from PIL import Image

from services.gemini_service import GeminiService


class ImageService:

    def __init__(self):

        self.gemini = GeminiService()

    def analyze_image(
        self,
        uploaded_file,
        prompt
    ):

        try:

            image = Image.open(uploaded_file)

            return self.gemini.generate_from_image(
                image=image,
                prompt=prompt
            )

        except Exception as error:

            return f"Image processing failed: {error}"