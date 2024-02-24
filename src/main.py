import streamlit as st
import datetime
import pandas as pd
import numpy as np


# サイドバーにページ選択のセレクトボックスを作成
page = st.sidebar.selectbox("ページを選択してください", ["入力", "グラフ出力"])

price = []
date = []
all_data = []
a=[[]]
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
        b = [edit_date, place]
        a.append(b)
        print(a)
        
        
        
        st.write(all_data)

    # 入力した要素をクリアする。
    def remove_data():
        price.clear()
        date.clear()


    place = st.number_input("価格を入力してください", 0, step=300)
    st.button("追加", on_click=lambda :add_data(place, d))
    st.button("クリア", on_click=remove_data)


elif page == "グラフ出力":
    hoge=[['12/1','9999'],['12/5','11111']]
    data = pd.DataFrame(
        hoge,columns=['日付','値段']
    )
    print(data)
    st.write('折れ線グラフ:')
    
    st.line_chart(data.set_index("日付"))