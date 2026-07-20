from google import genai
from google.genai import types

from config import Config


class GeminiService:

    def __init__(self):
        self.client = genai.Client(
            api_key=Config.GEMINI_API_KEY
        )
        self.model = "gemini-2.5-flash"

    def _generate(self, contents, config=None):

        response = self.client.models.generate_content(
            model=self.model,
            contents=contents,
            config=config
        )

        return response.text

    def generate_response(self, prompt):

        return self._generate(prompt)

    def generate_from_image(
        self,
        image,
        prompt
    ):

        return self._generate(
            [
                prompt,
                image
            ]
        )

    def generate_with_search(self, prompt):

        search_config = types.GenerateContentConfig(
            tools=[
                types.Tool(
                    google_search=types.GoogleSearch()
                )
            ]
        )

        return self._generate(
            prompt,
            search_config
        )

    def generate_from_pdf(
        self,
        context,
        question
    ):

        prompt = f"""
You are answering questions based ONLY on the uploaded PDF.

Context:
{context}

Question:
{question}

Instructions:
- Answer only using the given context.
- If the answer is not available in the context, reply:
"I couldn't find that information in the uploaded PDF."
"""

        return self._generate(prompt)