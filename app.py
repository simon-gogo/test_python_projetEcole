import streamlit as st
import pandas as pd

st.header("mon application")

st.title("Bonjour à tous !")
st.write('Mineure numérique')

nombres = [1, 2, 3, 4]
carre = [1**1, 2**2, 3**3, 4**4]

d = {"nombres" : nombres, "carré" : carre}
data = pd.DataFrame(d)

st.dataframe(data)
