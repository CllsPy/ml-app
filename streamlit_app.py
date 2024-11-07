import streamlit as st
import pandas as pd

# constants
URL_DATA = 'https://raw.githubusercontent.com/venky14/Machine-Learning-with-Iris-Dataset/refs/heads/master/Iris.csv'
st.title('Auto-Machine Learning')
st.info("A webapp based on pure Python that automacaly trains ML models on your data")

with st.expander ('Data'):
  st.write(*Raw Data*)
  df = pd.read_csv(URL_DATA)
  data
