import sqlite3
import streamlit as st
import pandas as pd

# Połączenie z bazą danych
conn = sqlite3.connect('db_temared.db')
cursor = conn.cursor()

# Pobierz informacje o kolumnach z tabeli
cursor.execute('PRAGMA table_info(technologies);')
columns = cursor.fetchall()

# Wyodrębnij nazwy kolumn
column_names = [column for column in columns]
df = pd.DataFrame(column_names)

# Wyświetl nazwy kolumn
st.write(df)

# Zamknij połączenie
conn.close()