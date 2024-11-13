import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

# Wczytanie pliku PDF
uploaded_file = "M.pdf"
pdf_viewer(uploaded_file, width=None)
