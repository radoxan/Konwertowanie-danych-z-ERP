import pandas as pd
import streamlit as st
import os

file_path = 'bend_parts.csv'

def add_row(name, number, material, thickness, length, width, bend_nums, radius, tool_exchange, side, schroder, henra, special, weight):
    file_exists = os.path.isfile(file_path)
    
    try:
        # Wczytanie istniejących danych, jeśli plik istnieje
        if file_exists:
            df = pd.read_csv(file_path, sep=',')
    except FileNotFoundError:
        # Jeśli plik nie istnieje, utwórz pusty DataFrame
        st.write("brak pliku bend_parts.csv")
    
    # Utworzenie nowego wiersza jako DataFrame
    new_row = pd.DataFrame([{
        'name': name, 
        'number': number, 
        'material': material, 
        'thickness': thickness, 
        'length': length, 
        'width': width, 
        'bend_nums': bend_nums, 
        'radius': radius, 
        'tool_exchange': tool_exchange, 
        'side': side, 
        'schroder': schroder, 
        'henra': henra, 
        'special': special,
    }])
    
    # Dodanie nowego wiersza do DataFrame za pomocą concat
    df = pd.concat([new_row], ignore_index=True)
    
    # Zapisanie zaktualizowanego DataFrame do pliku CSV
    df.to_csv(file_path, sep=',', index=False, mode= 'a', header=False)

# Aplikacja Streamlit
st.title('Obsługa danych detali giętych')
# Formularz do dodawania nowego wiersza
st.header('Dodaj nowy element')
length = 0
width = 0
weight = 0
with st.form(key='add_row_form'):
    col1_1, col1_2 = st.columns(2)
    with col1_1:
        number = st.text_input('Numer rysunkowy')
        material = st.selectbox('Materiał', ['CZARNA','OCYNK','ALU','ALU RYFL','ALU CZARNA'])
        length = st.text_input('Length')
        bend_nums = st.text_input('Ilość gięć')
        st.text(f'Auto-waga w kg')
        st.text(f'{length*width}')
    with col1_2:
        name = st.text_input('Nazwa elementu')
        thickness = st.text_input('Grubość')
        width = st.text_input('Width')
        radius = st.text_input('Promień gięcia')
        weight = st.text_input(f'Waga z rysunku {length}')
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        tool_exchange = st.checkbox('Tool Exchange')
    with col2:
        side = st.checkbox('Side')
    with col3:
        schroder = st.checkbox('Schroder')
    with col4:
        henra = st.checkbox('Henra')
    with col5:
        special = st.checkbox('Special')

    submit_button = st.form_submit_button(label='Dodaj element')

if submit_button:
    add_row(name, number, material, thickness, length, width, bend_nums, radius, tool_exchange, side, schroder, henra, special, weight)
    st.success('Wiersz został dodany pomyślnie!')