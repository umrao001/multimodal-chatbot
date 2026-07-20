import streamlit as st
import streamlit.components.v1 as components


class UI:

    # --------------------------------------------------
    # Hero Section
    # --------------------------------------------------

    @staticmethod
    def hero():

        st.markdown(
            """
            <style>

            .hero-card{
                width:100%;
                padding:40px;
                border-radius:28px;
                background:rgba(255,255,255,.05);
                border:1px solid rgba(255,255,255,.08);
                backdrop-filter:blur(20px);
                margin-bottom:20px;
            }

            .hero-title{
                font-size:54px;
                font-weight:800;
                color:white;
                margin-bottom:10px;
            }

            .hero-sub{
                font-size:18px;
                color:#bdbdbd;
                line-height:1.8;
            }

            .feature-card{

                border-radius:20px;
                padding:25px;
                background:rgba(255,255,255,.04);
                border:1px solid rgba(255,255,255,.06);
                text-align:center;
                transition:.3s;
                height:170px;

            }

            .feature-card:hover{

                transform:translateY(-6px);
                background:rgba(255,255,255,.07);

            }

            .feature-icon{

                font-size:42px;

            }

            .feature-title{

                font-size:22px;
                color:white;
                font-weight:700;

            }

            .feature-desc{

                color:#bbbbbb;
                font-size:15px;

            }

            .user-msg{

                background:#2563eb;
                padding:18px;
                border-radius:18px;
                color:white;
                margin-bottom:15px;

            }

            .assistant-msg{

                background:#1b1b1b;
                padding:18px;
                border-radius:18px;
                color:white;
                border:1px solid rgba(255,255,255,.08);
                margin-bottom:15px;

            }

            .typing{

                display:flex;
                gap:8px;
                padding:20px;

            }

            .typing span{

                width:10px;
                height:10px;
                border-radius:50%;
                background:#7c3aed;
                animation:bounce 1.2s infinite;

            }

            .typing span:nth-child(2){

                animation-delay:.2s;

            }

            .typing span:nth-child(3){

                animation-delay:.4s;

            }

            @keyframes bounce{

                0%{transform:translateY(0px);}
                50%{transform:translateY(-8px);}
                100%{transform:translateY(0px);}

            }

            </style>
            """,
            unsafe_allow_html=True
        )

        left, right = st.columns([1.3, 1])

        with left:

            st.markdown(
                """
                <div class="hero-card">

                <div class="hero-title">
                🤖 AI Assistant
                </div>

                <div class="hero-sub">

                Chat with AI.

                Search the web.

                Upload PDFs.

                Analyze Images.

                Solve calculations.

                Powered by Gemini 2.5 Flash.

                </div>

                </div>
                """,
                unsafe_allow_html=True
            )

        with right:

            components.html(
    """
    <iframe
    src="https://my.spline.design/robotfollowcursorforlandingpage-gK1QhAiY4mP6lKHv84xR0GdY/"
    frameborder="0"
    width="100%"
    height="420">
    </iframe>
    """,
    height=420,
)
            

    # --------------------------------------------------
    # Feature Cards
    # --------------------------------------------------

    @staticmethod
    def feature_cards():

        c1, c2, c3 = st.columns(3)

        with c1:

            st.markdown(
                """
                <div class="feature-card">

                <div class="feature-icon">
                💬
                </div>

                <div class="feature-title">
                AI Chat
                </div>

                <div class="feature-desc">
                Ask anything and receive intelligent responses.
                </div>

                </div>
                """,
                unsafe_allow_html=True
            )

        with c2:

            st.markdown(
                """
                <div class="feature-card">

                <div class="feature-icon">
                📄
                </div>

                <div class="feature-title">
                PDF Chat
                </div>

                <div class="feature-desc">
                Upload PDFs and ask questions instantly.
                </div>

                </div>
                """,
                unsafe_allow_html=True
            )

        with c3:

            st.markdown(
                """
                <div class="feature-card">

                <div class="feature-icon">
                📷
                </div>

                <div class="feature-title">
                Vision
                </div>

                <div class="feature-desc">
                Understand images using Gemini Vision.
                </div>

                </div>
                """,
                unsafe_allow_html=True
            )
                # --------------------------------------------------
    # Sidebar
    # --------------------------------------------------

    @staticmethod
    def sidebar():

        st.markdown(
            """
            <h2 style='text-align:center;'>
            🤖 AI Assistant
            </h2>
            """,
            unsafe_allow_html=True
        )

        st.caption("Your Personal Multimodal AI")

    # --------------------------------------------------
    # Upload Section
    # --------------------------------------------------

    @staticmethod
    def upload_section():

        st.markdown(
            """
            <div style="padding:12px 0px;">
                <h3>📂 Upload Files</h3>
            </div>
            """,
            unsafe_allow_html=True
        )

    # --------------------------------------------------
    # User Bubble
    # --------------------------------------------------

    @staticmethod
    def user_message(message):

        st.markdown(
            f"""
            <div class="user-msg">
            {message}
            </div>
            """,
            unsafe_allow_html=True
        )

    # --------------------------------------------------
    # Assistant Bubble
    # --------------------------------------------------

    @staticmethod
    def assistant_message(message):

        st.markdown(
            f"""
            <div class="assistant-msg">
            {message}
            </div>
            """,
            unsafe_allow_html=True
        )

    # --------------------------------------------------
    # Typing Animation
    # --------------------------------------------------

    @staticmethod
    def typing():

        st.markdown(
            """
            <div class="typing">
                <span></span>
                <span></span>
                <span></span>
            </div>
            """,
            unsafe_allow_html=True
        )

    # --------------------------------------------------
    # Status Card
    # --------------------------------------------------

    @staticmethod
    def status_card(title, value, icon="✨"):

        st.markdown(
            f"""
            <div style="
                padding:18px;
                border-radius:18px;
                background:rgba(255,255,255,.04);
                border:1px solid rgba(255,255,255,.08);
                margin-bottom:12px;
            ">

            <h4 style="margin:0;">
                {icon} {title}
            </h4>

            <p style="
                color:#bdbdbd;
                margin-top:8px;
                margin-bottom:0;
            ">
                {value}
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    # --------------------------------------------------
    # Divider
    # --------------------------------------------------

    @staticmethod
    def section(title):

        st.markdown(
            f"""
            <h3 style="
                margin-top:25px;
                margin-bottom:20px;
            ">
            {title}
            </h3>
            """,
            unsafe_allow_html=True
        )

    # --------------------------------------------------
    # Empty Chat
    # --------------------------------------------------

    @staticmethod
    def empty_chat():

        st.markdown(
            """
            <div style="
                padding:70px;
                text-align:center;
                color:#bdbdbd;
            ">

            <h2>
            👋 Welcome
            </h2>

            <p>
            Start a conversation with your AI Assistant.
            <br><br>
            Upload a PDF, image, or simply ask a question.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    # --------------------------------------------------
    # Footer
    # --------------------------------------------------

    @staticmethod
    def footer():

        st.markdown("<br><br>", unsafe_allow_html=True)

        st.markdown(
            """
            <hr style="opacity:.2;">

            <div style="
                text-align:center;
                color:#8a8a8a;
                padding-bottom:20px;
                font-size:14px;
            ">

            Built with ❤️ using

            <b>Streamlit</b> •
            <b>Gemini 2.5 Flash</b> •
            <b>FAISS</b> •
            <b>Sentence Transformers</b>

            </div>
            """,
            unsafe_allow_html=True
        )