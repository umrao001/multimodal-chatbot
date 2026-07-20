import streamlit as st
from pathlib import Path


class ThemeManager:

    DARK = "dark"
    LIGHT = "light"

    @staticmethod
    def initialize():

        if "theme" not in st.session_state:
            st.session_state.theme = ThemeManager.DARK

    @staticmethod
    def current():

        return st.session_state.theme

    @staticmethod
    def is_dark():

        return st.session_state.theme == ThemeManager.DARK

    @staticmethod
    def set(theme):

        st.session_state.theme = theme

    @staticmethod
    def toggle():

        if ThemeManager.is_dark():
            st.session_state.theme = ThemeManager.LIGHT
        else:
            st.session_state.theme = ThemeManager.DARK

    @staticmethod
    def switcher():

        st.markdown("### 🎨 Theme")

        cols = st.columns(2)

        with cols[0]:

            if st.button(
                "🌙 Dark",
                use_container_width=True
            ):
                ThemeManager.set(
                    ThemeManager.DARK
                )
                st.rerun()

        with cols[1]:

            if st.button(
                "☀ Light",
                use_container_width=True
            ):
                ThemeManager.set(
                    ThemeManager.LIGHT
                )
                st.rerun()

    @staticmethod
    def apply():

        css_folder = Path("assets")

        if ThemeManager.is_dark():

            css_file = css_folder / "dark.css"

        else:

            css_file = css_folder / "light.css"

        if css_file.exists():

            with open(css_file, "r") as f:

                st.markdown(
                    f"<style>{f.read()}</style>",
                    unsafe_allow_html=True
                )