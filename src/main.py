import streamlit as st

st.title("入力したデータをグラフにする")

# cache化するため
@st.cache_resource
def cache_lst():
    lst = []
    return lst

price = cache_lst()

# 要素を追加する。（値段を追加する）
def add_data(place):
    price.append(place)
    st.write(price)

# 入力した要素をクリアする。
def remove_data():
    price.clear()


place = st.number_input("2023年1月", 0, step=300)
st.button("追加", on_click=lambda :add_data(place))
st.button("クリア", on_click=remove_data)