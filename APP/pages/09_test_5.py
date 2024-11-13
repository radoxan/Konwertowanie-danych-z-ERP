import streamlit as st

if 'page_number' not in st.session_state:
    st.session_state.page_number = 1

def page_up(page_number):
    if page_number == 4:
        page_number = 1
        return page_number
    else:
        page_number = page_number + 1
    return page_number

def page_down(page_number):
    if page_number == 1:
        page_number = 4
        return page_number
    else:
        page_number = page_number - 1
    return page_number

def next_page_def():
    st.session_state.page_number = page_up(st.session_state.page_number)
    st.rerun()


st.write(f"{st.session_state.page_number}")

if 'number' not in st.session_state:
    st.session_state.number = ''

if 'name' not in st.session_state:
    st.session_state.name = ''

if 'length' not in st.session_state:
    st.session_state.length = ''

if 'width' not in st.session_state:
    st.session_state.width = ''

number = st.session_state.number
name = st.session_state.name
length = st.session_state.length
width = st.session_state.width

if st.session_state.page_number == 1:
    st.session_state.number = st.text_input("Podaj numer", value=st.session_state.number)
elif st.session_state.page_number == 2:
    st.session_state.name = st.text_input("Podaj nazwę", value=st.session_state.name)
elif st.session_state.page_number == 3:
    st.session_state.length = st.text_input("Podaj długość", value=st.session_state.length)
elif st.session_state.page_number == 4:
    st.session_state.width = st.text_input("Podaj szerokość", value=st.session_state.width)
else:
    st.header("koniec zakresu")

col1, col2 = st.columns(2)
with col1:
    next_page = st.button("Następna strona")
    if next_page:
        next_page_def()
with col2:
    previous_page = st.button("Poprzednia strona")
    if previous_page:
        st.session_state.page_number = page_down(st.session_state.page_number)
        st.rerun()

if number != st.session_state.number:
    next_page_def()

st.write(f"Numer: {st.session_state.number}")
st.write(f"Nazwa: {st.session_state.name}")
st.write(f"Długość: {st.session_state.length}")
st.write(f"Szerokość: {st.session_state.width}")