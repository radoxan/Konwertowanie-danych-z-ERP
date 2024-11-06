import streamlit as st
import sqlite3
import pandas as pd

st.title("Podgląd danych")
base_name = "db_temared.db"
st.header(f"Baza danych: {base_name}")
# Połączenie z bazą danych
conn = sqlite3.connect(f'{base_name}')

# Utworzenie kursora
cursor = conn.cursor()

# Wykonanie zapytania do sqlite_master, aby pobrać nazwy tabel
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Pobranie wszystkich wyników
tabele = cursor.fetchall()

# Wyświetlenie nazw tabel
lista = []
for tabela in tabele:
   lista.append(tabela)
st.write("Lista tabel znajdujących się w bazie:")
st.table(lista)

# Wczytanie danych z tabeli
with sqlite3.connect(f'{base_name}') as conn:
        df3 = pd.read_sql("SELECT * FROM technologies", conn)
st.write('Dane wczytane z bazy danych dla technologii:')
st.dataframe(df3)

# Wczytanie danych z tabeli
with sqlite3.connect(f'{base_name}') as conn:
        df4 = pd.read_sql("SELECT * FROM bend_parts", conn)
st.write('Dane wczytane z bazy danych dla detali giętych:')
st.dataframe(df4)


# Zamknięcie połączenia
conn.close()