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
st.dataframe(df2, hide_index=True)
conn.close()

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

# Funkcja pobiera nazwę kolumny, szuka jej w tabeli i zwraca posortowane wartości bez duplikatów 
def get_list_from_column(column_name):
        # Wyodrębnia kolumnę z DataFrame
        column_material = df2[column_name]
        # Dane z kolumny zamienia na listę, usuwa duplikaty oraz wartości NONE
        column_material_duplicatesdeleted = list(set(column_material.dropna()))
        # Sortuje Dane
        column_material_duplicatesdeleted_sorted = sorted(column_material_duplicatesdeleted, reverse=False)
        # Wyświetla dane posortowane
        return column_material_duplicatesdeleted_sorted

# Funkcja przypisuje długość elementu do właściwego zakresu
def check_length(length):
    if length <= 500:
        return 'l_1_-_500'
    elif length <= 1000:
        return 'l_500_-_1000'
    elif length <= 1500:
        return 'l_1000_-_1500'
    elif length <= 2000:
        return 'l_1501_-_2000'
    elif length <= 3000:
        return 'l_2001_-_3000'
    elif length <= 4100:
        return 'l_3001_-_4100'
    elif length <= 6000:
        return 'l_4101_-_6000'                
    else:
        return 'Element zbyt długi'

# Funkcja sprawdza czy wprowadzona ilość jest równa "1", zwraca "Prawda" lub "Fałsz"
def if_one_bend(bend_nums):
    if bend_nums == '1' :
        return 'Prawda'
    else:
        return 'Fałsz'

# Z warości True lub False zwraca wartość tekstową "Prawda" lub "Fałsz"
def true_false(t_or_f):
    if t_or_f:
        return "Prawda"
    else:
        return "Fałsz"

col1, col2 =st.columns(2)
with col1:
    column_name_1 = 'material'
    list_1 = get_list_from_column(column_name_1)
    material = st.radio("Wybierz materiał:",list_1, horizontal=True)
with col2:    
    st.title(material)

col1, col2 = st.columns(2)
with col1:
    column_name_2 = 'radius'
    list_2 = get_list_from_column(column_name_2)
    radius = st.radio("Wybierz promień:",list_2, horizontal=True)
with col2:
    st.title(f"R {radius}")

col1, col2, col3 = st.columns([1,1,2])
with col1:
    length = st.number_input("Podaj długość elementu")
    result = check_length(length)
with col3:
    st.title(result)

col1, col2 = st.columns(2)
with col1:
    bend_nums = st.radio("Wybierz ilość gięć:",['1','2','3','4','5','6','7','8','9'], horizontal=True)
    one_bend = if_one_bend(bend_nums)
with col2:
    st.title(one_bend)

col1, col2 = st.columns(2)
with col1:
    tool_exchange = st.checkbox('Czy detal wymaga innego zazbrojenia maszyny niż standardowe')
with col2:
    st.write(true_false(tool_exchange))

col1D, col2D = st.columns(2)
with col1:
    side = st.checkbox('Czy detal jest burtą')
with col2:
    st.write(true_false(side))

col1, col2 = st.columns(2)
with col1:
    schroder = st.checkbox('Czy detal jest gięty na Schroder')
with col2:
    st.write(true_false(schroder))

col1, col2 = st.columns(2)
with col1:
    henra = st.checkbox('Czy detal jest z Henry')
with col2:
    st.write(true_false(henra))

col1, col2 = st.columns(2)
with col1:
    special = st.checkbox('Czy detal jest wykonywany na narzędziu specjalnym')
with col2:
    st.write(true_false(special))

col1, col2 = st.columns(2)
with col1:
    profiled = st.checkbox('Czy detal jest profilowany na Temabend')
with col2:
    st.write(true_false(profiled))