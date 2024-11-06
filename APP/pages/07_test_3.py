import pandas as pd
import streamlit as st

col1, col2, col3 = st.columns(3)
with col1:
    material = st.radio("Wybierz materiał:",['ocynk','czarna',])
with col2:
    thickness = st.radio("Wybierz grubość:",['1','2','3'])
with col3:
    length = st.radio("Wybierz materiał:",['0-500','501-1000',])

data = [['ocynk', '1', '0-500', 'Tech_A'],
        ['ocynk', '2', '0-500', 'Tech_B'],
        ['ocynk', '3', '0-500', 'Tech_C'],
        ['ocynk', '1', '501-1000', 'Tech_D'],
        ['ocynk', '2', '501-1000', 'Tech_E'],
        ['ocynk', '3', '501-1000', 'Tech_F'],
        ['czarna', '1', '0-500', 'Tech_G'],
        ['czarna', '2', '0-500', 'Tech_H'],
        ['czarna', '3', '0-500', 'Tech_I'],
        ['czarna', '1', '501-1000', 'Tech_J'],
        ['czarna', '2', '501-1000', 'Tech_K'],
        ['czarna', '3', '501-1000', 'Tech_L']]

df_1 = pd.DataFrame(data, columns=['material','thickness','length','tech'])

st.dataframe(df_1)

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
    
tech = find_value(df_1, material, thickness, length)
st.write(tech)

