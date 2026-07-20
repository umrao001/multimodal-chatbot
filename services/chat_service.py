from services.gemini_service import GeminiService
from services.image_service import ImageService
from services.search_service import SearchService
from services.tool_service import ToolService


class ChatService:

    def __init__(self):

        self.gemini = GeminiService()
        self.image_service = ImageService()

    def send_message(
        self,
        prompt,
        image=None,
        rag=None
    ):

        prompt = prompt.strip()

        if not prompt:
            return "Please enter a message."

        if image:
            return self.image_service.analyze_image(
                uploaded_file=image,
                prompt=prompt
            )

        if rag and rag.has_index():

            context = rag.retrieve(prompt)

            return self.gemini.generate_from_pdf(
                context=context,
                question=prompt
            )

        tool_response = ToolService.execute(prompt)

        if tool_response:
            return tool_response

        if SearchService.is_search_query(prompt):
            return self.gemini.generate_with_search(prompt)

        return self.gemini.generate_response(prompt)