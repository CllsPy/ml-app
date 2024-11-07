import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# constants
URL_DATA = 'https://raw.githubusercontent.com/venky14/Machine-Learning-with-Iris-Dataset/refs/heads/master/Iris.csv'
st.title('Auto-Machine Learning')
st.info("Um WEB-APP que automaticamente treina modelos de Machine Learning!")

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
  spl = st.slider('Sepal Length em Cm', 0.0, 100.0)
  spw = st.slider('Sepal Width Cm', 0.0, 100.0)
  ptl = st.slider('Petal Length Cm', 0.0, 100.0)
  plw = st.slider('Petal Width Cm', 0.0, 100.0)

  # generate a dataframe with input data
  data = {'SepalLengthCm': spl, 'SepalWidthCm': spw, 'PetalLengthCm': ptl, 'PetalWidthCm': plw}
  input_data = pd.DataFrame(data, index=[0])

with st.expander('Novos Dados'):
  input_data


with st.expander('Previsões'):
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
  model = RandomForestClassifier()
  model.fit(X_train, y_train)
  y_h = model.predict(input_data)
  y_h


