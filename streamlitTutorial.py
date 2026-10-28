import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello, Streamlit!")
st.write(":streamlit: This is your first Streamlit app")
st.text("Lets get started")

#conditional logic with widgets

name = st.text_input("Enter your name:")
if st.button("Greet"):
    st.success(f"Hello, {name}!")

#Displaying Data and charts
df=pd.DataFrame(np.random.randn(10,2),columns=['A','B'])
st.line_chart(df)
st.bar_chart(df)

#File uploading and caching topics

upload_file = st.file_uploader("upload a csv", type='csv')
if upload_file:
    df = pd.read_csv(upload_file)
    st.dataframe(df)

st.title("Text and markdown Demo")
st.header("This is a header")
st.subheader("This is a subheader")
st.markdown("**Bold**,*Italic*,`Code`,[Link](https://streamlit.io)")
st.code("for i in range(5): print(i)",language="Python")

st.text_input("What's your name?")
st.text_area("Write something...")
st.number_input("Pick a number", min_value=0, max_value=100)
st.slider("Choose a range", 0, 100)
st.selectbox("Select a fruit", ["Apple", "Banana", "Mango"])
st.multiselect("Choose toppings", ["Cheese", "Tomato", "Olives"])
st.radio("Pick one",["Option A","Option B"])
st.checkbox("I agree to the terms")
