import streamlit as st
import pandas as pd

# constants
URL_DATA = 'https://raw.githubusercontent.com/venky14/Machine-Learning-with-Iris-Dataset/refs/heads/master/Iris.csv'
st.title('Auto-Machine Learning')
st.info("A webapp based on pure Python that automacaly trains ML models on your data")

with st.expander ('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv(URL_DATA)
  df

  st.write('**Features**')
  X = df.iloc[:, 1:5]
  X

  st.write('**Target**')
  y = df.iloc[:, 5:]
  y

# SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm,Species
with st.expander('Data Vis'):
  st.write('**ScatterPlot**')
  st.scatter_chart(data=df, x='SepalLengthCm', y='PetalLengthCm', color='Species')
  st.scatter_chart(data=df, x='SepalWidthCm', y='PetalWidthCm', color='Species')

with st.sidebar:
  st.header('Input')
  spl = st.slider('Sepal Length em Cm', 0.1, 20)
