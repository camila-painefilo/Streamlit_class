import streamlit as st

st.title("Title 1")
st.header("Header")
st.markdown("""
markdown
**markdown**
*markdown*
""")
st.write("hello! World")

a = st.number_input("escribe un numero", step = 1)
b = st.text_input("escribe texto")

st.write(a)
st.write(b)

for i in range (a):
  total +=i
  st.write(total)
