import streamlit as st
import joblib
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error
import matplotlib.dates as mdates
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split


st.markdown("# Modelo preditivo do petróleo brent! ")

with open('./models/modelo.pkl', 'rb') as file_2:
    modelo_brent = joblib.load(file_2)


# Carregar o DataFrame
df = pd.read_csv('./data/dados.csv')
df = df.drop('Unnamed: 0', axis=1)
df['Data'] = pd.to_datetime(df['Data'], format="%d/%m/%Y")
df.columns = ['ds', 'y']
df.y = pd.to_numeric(df.y)
df = df.sort_values(by='ds', ascending=True).reset_index(drop=True)

st.dataframe(df)

treino = df.sample(frac=0.8, random_state=0)
teste = df.drop(treino.index)

dff = modelo_brent.make_future_dataframe(periods=240, freq='B')
previsao = modelo_brent.predict(dff)

previsao = previsao[['ds', 'yhat']]
valores_reais = treino[['ds', 'y']]

resultados = pd.merge(previsao, valores_reais, on='ds', how='inner')

modelo_brent.plot(previsao, figsize=(20,6))
plt.plot(teste['ds'], teste['y'], '.r')

