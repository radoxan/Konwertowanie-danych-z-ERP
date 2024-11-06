import pandas as pd
import streamlit as st

# Przykładowy DataFrame
data = {'material': ['wood', 'metal', 'plastic', 'wood', 'metal']}
df2 = pd.DataFrame(data)

# Wyodrębnij kolumnę 'material'
column_material = df2['material']

# Usuń duplikaty i zamień na listę
column_material_duplicatesdeleted = list(set(column_material))

# Posortuj listę w odwrotnej kolejności
column_material_duplicatesdeleted_sorted = sorted(column_material_duplicatesdeleted, reverse=True)

# Wyświetl wynik
st.write(column_material_duplicatesdeleted_sorted)