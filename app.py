import streamlit as st

from services.chat_service import ChatService
from services.pdf_service import PDFService
from services.rag_service import RAGService

from utils.theme import ThemeManager
from utils.ui import UI


st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


ThemeManager.initialize()
ThemeManager.apply()


if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_service" not in st.session_state:
    st.session_state.chat_service = ChatService()

if "rag_service" not in st.session_state:
    st.session_state.rag_service = RAGService()

if "uploaded_image" not in st.session_state:
    st.session_state.uploaded_image = None

if "uploaded_pdf" not in st.session_state:
    st.session_state.uploaded_pdf = None

if "uploaded_pdf_name" not in st.session_state:
    st.session_state.uploaded_pdf_name = None


chat_service = st.session_state.chat_service
rag_service = st.session_state.rag_service


# --------------------------
# Hero
# --------------------------

UI.hero()

st.markdown("<br>", unsafe_allow_html=True)

UI.feature_cards()

st.markdown("<br>", unsafe_allow_html=True)


# --------------------------
# Sidebar
# --------------------------

with st.sidebar:

    UI.sidebar()

    st.divider()

    ThemeManager.switcher()

    st.divider()

    UI.upload_section()

    uploaded_image = st.file_uploader(
        "📷 Upload Image",
        type=[
            "png",
            "jpg",
            "jpeg"
        ]
    )

    if uploaded_image is not None:

        st.session_state.uploaded_image = uploaded_image

        st.image(
            uploaded_image,
            use_container_width=True
        )

    uploaded_pdf = st.file_uploader(
        "📄 Upload PDF",
        type=["pdf"]
    )

    if uploaded_pdf is not None:

        st.session_state.uploaded_pdf = uploaded_pdf

        st.success(uploaded_pdf.name)

        if (
            st.session_state.uploaded_pdf_name
            != uploaded_pdf.name
        ):

            with st.spinner(
                "Indexing PDF..."
            ):

                pdf_text = PDFService.extract_text(
                    uploaded_pdf
                )

                rag_service.build_index(
                    pdf_text
                )

                st.session_state.uploaded_pdf_name = (
                    uploaded_pdf.name
                )

            st.success(
                "PDF indexed successfully."
            )

    st.divider()

    st.markdown("### 🚀 Features")

    st.markdown(
        """
        - 💬 AI Chat
        - 🌍 Google Search
        - 📄 PDF Chat
        - 📷 Image Understanding
        - 🧮 Calculator
        - 📅 Date & Time
        """
    )

    st.divider()

    if st.button(
        "🗑 Clear Chat",
        use_container_width=True
    ):

        st.session_state.messages = []

        rag_service.clear()

        st.session_state.uploaded_image = None

        st.session_state.uploaded_pdf = None

        st.session_state.uploaded_pdf_name = None

        st.rerun()


# --------------------------
# Chat History
# --------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(
            message["content"]
        )


# --------------------------
# Chat Input
# --------------------------

prompt = st.chat_input(
    "💬 Ask me anything..."
)
if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):

        UI.user_message(prompt)

    with st.chat_message("assistant"):

        placeholder = st.empty()

        with placeholder.container():

            UI.typing()

        try:

            response = chat_service.send_message(
                prompt=prompt,
                image=st.session_state.uploaded_image,
                rag=rag_service
            )

        except Exception as error:

            response = f"❌ {error}"

        placeholder.empty()

        UI.assistant_message(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )


st.markdown("<br>", unsafe_allow_html=True)

UI.footer()