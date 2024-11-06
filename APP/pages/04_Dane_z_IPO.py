import streamlit as st
import pandas as pd

st.title("Dane z IPO")
file_path = 'dane_z_ipo.csv'
df_ipo = pd.read_csv(file_path, sep=';')
st.write(df_ipo)