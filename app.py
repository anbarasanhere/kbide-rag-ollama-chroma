import streamlit as st

from config import settings
from components.sidebar import Sidebar
from components.chat import ChatComponent

# -----------------------------------------------------

st.set_page_config(
    page_title=settings.APP_TITLE,
    page_icon=settings.PAGE_ICON,
    layout=settings.LAYOUT
)

# -----------------------------------------------------

Sidebar().render()

ChatComponent().render()
