import streamlit as st
import sqlite3
import pandas as pd


# Połączenie z bazą danych
data_base = 'db_temared.db'
conn = sqlite3.connect(f'{data_base}')

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
st.table(lista)

# Wczytanie danych z tabeli
with sqlite3.connect(f'{data_base}') as conn:
        df2 = pd.read_sql("SELECT * FROM technologies", conn)
st.write('Technologie wczytane z bazy danych:')
st.dataframe(df2)

def find_value(df, material, thickness, length):
    # Filtrujemy DataFrame na podstawie podanych wartości
    filtered_df = df[(df['material'] == material) & 
                     (df['thickness'] == thickness) & 
                     (df['length'] == length)]
    
    # Sprawdzamy, czy znaleziono odpowiedni wiersz
    if not filtered_df.empty:
        # Zwracamy wartość z ostatniej kolumny
        return filtered_df.iloc[0, -1]
    else:
        return None

# Zamknięcie połączenia
conn.close()

