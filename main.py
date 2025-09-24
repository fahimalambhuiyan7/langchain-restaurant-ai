import streamlit as st 
from langchain_helper import generate_resturant

st.title("Resturant Name Generator")
cuisine = st.sidebar.selectbox("Pick a cuisine",("Mexican","Italian","South Indian","North Indian","American","chinese","Japanese","Egypt","asgard"))


if cuisine:
    response = generate_resturant(cuisine)
    st.header(response['resturant_names'])
    item_lst = response['menu_items'].split(",")
    st.write("**Menu**")
    for item in item_lst:
        st.write("-",item)
