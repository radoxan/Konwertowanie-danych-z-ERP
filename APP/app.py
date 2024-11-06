import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

st.set_page_config(
    page_title="Moja Aplikacja Streamlit",
    page_icon=":shark:",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title("Witaj w aplikacji do obsługi danych detali giętych")

st.sidebar.title("Menu")
st.sidebar.write("Wybierz zakładkę z menu bocznego.")
