import streamlit as st
import pandas as pd
import os
from streamlit_pdf_viewer import pdf_viewer

# Program wyszukuje rysunki techniczne na podstawie fragmetu tekstu. 
# Wyświetla listę plików spełniających kryteria.
# Po wybraniu szukanej opcji lub wpisaniu pełnego numeru wyświetla szukany rysunek. 
# Wyświetla także wszystkie odnalezione poprawki danego rysunku. Domyślnie najnowszą.

# Metoda zwracająca pełną ścieżkę do pliku
def get_file_path_full(file_name):
    base_path = r"X:\Tech\DOKUMENTACJA W PRODUKCJI"
    folder_name = file_name.split('.')[0]
    file_path_full = f"{base_path}\\{folder_name}\\{file_name}.PDF"
    return file_path_full

# Metoda zwracająca ścieżkę do folderu
def get_file_path_folder(file_name):
    base_path = r"X:\Tech\DOKUMENTACJA W PRODUKCJI"
    folder_name = file_name.split('.')[0]
    file_path_folder = f"{base_path}\\{folder_name}\\"
    return file_path_folder

# Funkcja zwracająca listę wszytskich nazw plików zawartych w katalogu podanum jako argument
def list_files_in_directory(directory):
    try:
        # Pobieranie listy plików w danym folderze
        files = os.listdir(directory)
        return files
    except FileNotFoundError:
        return "Podany folder nie istnieje."
    except PermissionError:
        return "Brak uprawnień do odczytu folderu."


# Metoda wyszukująca wszystkie poprawki w danej lokalizacji i zwracająca je w postaci tabeli
def find_files(base_name, directory):
    found_files = []

    # Sprawdzenie pliku bez końcówki
    file_path = os.path.join(directory, f"{base_name}.pdf")
    if os.path.isfile(file_path):
        found_files.append(file_path)

    # Sprawdzenie plików z końcówkami od "_00.00.pdf" do "_25.25.pdf"
    for i in range(26):
        for j in range(26):
            file_name = f"{base_name}_{i:02}.{j:02}.pdf"
            file_path = os.path.join(directory, file_name)
            if os.path.isfile(file_path):
                found_files.append(file_path)

    return found_files

#Fukncja do usuwania wszystkiego po ostatniej kropce
def remove_after_last_dot(text):
    last_dot_index = text.rfind('.')
    if last_dot_index != -1:
        return text[:last_dot_index]
    return text

#Fukncja do usuwania wszystkiego po znaku "_"
def remove_after_last_sign(text):
    last_sign_index = text.rfind('_')
    if last_sign_index != -1:
        return text[:last_sign_index]
    return text

# Funkcja do wyszukiwania wierszy na podstawie fragmentu kolumny "number"
def search_by_number_fragment(number_fragment, number_list):
    return [number for number in number_list if number_fragment in number]

# Funkcja usuwająca duplikaty z listy
def remove_duplicates(input_list):
    seen = set()
    unique_list = []
    for item in input_list:
        if item not in seen:
            unique_list.append(item)
            seen.add(item)
    return unique_list

col1, col2 = st.columns([2,5])
with col1:
    #Bloki elementów Streamlit
    st.header('Wyszukaj indeks')
    search_number = st.text_input('Wprowadź numer do wyszukania')
    search_button = st.button('Szukaj')


    folder_path = get_file_path_folder(search_number)
    options=list_files_in_directory(folder_path)
    options_cleared_dot = [remove_after_last_dot(option) for option in options]
    options_cleared_sign = [remove_after_last_sign(option_cleared_sign) for option_cleared_sign in options_cleared_dot]
    options_without_duplicates = remove_duplicates(options_cleared_sign)
    fragmet_options = search_by_number_fragment(search_number, options_without_duplicates)
    choosen_draw = st.selectbox("Wybierz jeden z poniższych plików", fragmet_options)
    file_name = f"{choosen_draw}"
    folder_name = file_name.split('.')[0]
    choosen_draw_cleared = choosen_draw.split('_')[0]
    base_name = f"{choosen_draw_cleared}"
    directory = f"{get_file_path_folder(file_name)}"

    # st.write(base_name)
    # st.write(directory)

    found_files = find_files(base_name, directory)


    #if found_files:
    #    print("Znalezione pliki:")
    #    for file in found_files:
    #        print(file)
    #else:
    #    print("Nie znaleziono plików.")

    # st.write(f"{found_files}")

    sorted_found_files = found_files.sort(reverse=True)
    select_correct = st.radio("Wybierz poprawkę", found_files)

with col2:   
    try:
        with pdf_viewer(f"{select_correct}"): #Wyświetla rysunek techniczny
            pdf_viewer(f"{select_correct}")
    except FileNotFoundError:
        st.write("Nie odnaleziono rysunku.")


