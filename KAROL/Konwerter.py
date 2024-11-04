import streamlit as st
import pandas as pd
from datetime import datetime
from openpyxl import load_workbook

# Program konwertuje dane
def save_to_excel(df):
    df = df.to_excel('plik.xlsx', index=False)
    # Załaduj plik Excel
    wb = load_workbook('plik.xlsx')
    ws = wb.active
    ws.column_dimensions['A'].width = 15
    ws.column_dimensions['B'].width = 30
    ws.column_dimensions['C'].width = 4
    ws.column_dimensions['D'].width = 15
    ws.column_dimensions['E'].width = 15
    ws.column_dimensions['F'].width = 15
    ws.column_dimensions['G'].width = 15
    wb.save('plik.xlsx')
    return wb

def get_time():
    now = datetime.now()
    formatted_date = now.strftime('%d-%m-%Y %H:%M:%S')
    return formatted_date

def clear_table(df):
    df = df.iloc[17:-10]
    df['Unnamed: 3'] = df['Unnamed: 3'].shift(-1)
    df = df.dropna(axis=1, how='all')
    df = df.dropna(how='all')
    df.columns = ['Indeks', 'Nazwa', 'Jm', 'Ilość do sprzed.', 'Ilość w mag', 'Wartość księgowa', 'Wartość rzeczywista']

    return df

st.title('Strona konwertująca plik Excel wygenerowany z ERP')
file_1 = st.file_uploader('Wybierz plik Excel do wyświetlenia:')
if file_1 is not None:
    df_1 = pd.read_excel(file_1)
    st.write("Dane wczytane z pliku excel:")
    st.dataframe(df_1, use_container_width=True, hide_index=True)
    st.write("Dane przetworzone i przygotowane do zapisu")
    df_2 = clear_table(df_1)
    st.dataframe(df_2, use_container_width=True, hide_index=True)

    file_name = f"Dane z ERP {get_time()}"
    save_to_excel(df_2)
    st.download_button(
        label="Pobierz plik Excel",
        data=open('plik.xlsx', 'rb').read(),
        file_name=f'{file_name}.xlsx',
        mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
else:
    st.warning("Prześlij plk Excel wygenerowany z ERP w formacie .xls lub .xlsx")

st.markdown('<div style="text-align: right;">Powered by Radosław Krupa</div>', unsafe_allow_html=True)