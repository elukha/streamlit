import streamlit as st
import datetime
import pandas as pd
import numpy as np

def convert_1d_to_2d(l, cols):
    return [l[i:i + cols] for i in range(0, len(l), cols)]

# サイドバーにページ選択のセレクトボックスを作成
page = st.sidebar.selectbox("ページを選択してください", ["入力", "グラフ出力"])

price = []
date = []
all_data = []

# 選択されたページを表示
if page == "入力":
    st.title("入力したデータをグラフにする")

    # cache化するため
    @st.cache_resource
    def all_cache_lst():
        lst = []
        return lst

    all_data = all_cache_lst()

    min_date = datetime.date(1900, 1, 1)
    max_date = datetime.date(2100, 1, 1)
    d = st.date_input('年月日を入力してください', min_value=min_date, max_value=max_date)

    # 要素を追加する。（値段と日付を追加する）
    def add_data(place, d):
        year = d.year
        month = d.month
        day = d.day
        edit_date = f"{year}-{month}-{day}"
        
        all_data.extend([place, edit_date])
        
        st.write(all_data)

    # 入力した要素をクリアする。
    def remove_data():
        price.clear()
        date.clear()


    place = st.number_input("価格を入力してください", 0, step=300)
    st.button("追加", on_click=lambda :add_data(place, d))
    st.button("クリア", on_click=remove_data)


elif page == "グラフ出力":
    two_array = convert_1d_to_2d(all_data, 2)
    data = pd.DataFrame(

    )
    print(data)
    st.write('折れ線グラフ:')
    st.line_chart(data.set_index("日付"))