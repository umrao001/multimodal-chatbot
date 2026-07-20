import fitz


class PDFService:

    @staticmethod
    def extract_text(uploaded_file):

        try:

            pdf = fitz.open(
                stream=uploaded_file.read(),
                filetype="pdf"
            )

            pages = []

            for page in pdf:

                text = page.get_text("text").strip()

                if text:
                    pages.append(text)

            pdf.close()

            return "\n\n".join(pages)

        except Exception as error:

            raise Exception(
                f"Unable to read PDF: {error}"
            )