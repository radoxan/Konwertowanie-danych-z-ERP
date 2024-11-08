import streamlit as st

def wycena_1(weight, bend_nums, price):
    w = (weight*0.1)+((bend_nums-1.0)*(price-((bend_nums-1)*0.01)))
    if w < 0:
        w = 0
    return w

def wycena_2(bend_nums, price):
    w = (price-((bend_nums-1)*0.01))*bend_nums
    if w < 0:
        w = 0
    return w

def wycena_3(weight, bend_nums, multi):
    w = (weight*0.1)*(1.0+(multi*(bend_nums-1)))
    if w < 0:
        w = 0
    return w

def wycena_max(weight, bend_nums, price, multi):
    w1 = wycena_1(weight, bend_nums, price)
    w2 = wycena_2(bend_nums, price)
    w3 = wycena_3(weight, bend_nums, multi)
    w_max = max(w1,w2,w3)
    return w_max

col1, col2 = st.columns([3,1])
with col1:
    weight = st.number_input("Podaj wagę",min_value=0.0,value=0.0,step=0.01,format="%0.2f")
with col2:
    st.text(weight)

col1, col2 = st.columns([3,1])
with col1:
    bend_nums = st.number_input("Podaj ilość gięć",min_value=0,value=0,step=1,format="%d")
with col2:
    st.text(bend_nums)

col1, col2 = st.columns([3,1])
with col1:
    price = st.number_input("Podaj minimalną cenę",min_value=0.0,value=0.0,step=0.01,format="%0.2f")
with col2:
    st.text(price)

col1, col2 = st.columns([3,1])
with col1:
    multi = st.number_input("Podaj współczynnik",min_value=0.0,value=0.0,step=0.01,format="%0.2f")
with col2:
    st.text(multi)

price_sum = wycena_max(weight, bend_nums, price, multi)

st.title(f"Wycena elementu to: {price_sum:.5f}")

price_1 = wycena_1(weight, bend_nums, price)
st.header(f"Wycena 1: {price_1:.2f}")
price_2 = wycena_2(bend_nums, price)
st.header(f"Wycena 2: {price_2:.2f}")
price_3 = wycena_3(weight, bend_nums, multi)
st.header(f"Wycena 3: {price_3:.2f}")