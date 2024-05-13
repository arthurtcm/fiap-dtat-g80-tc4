import pandas as pd
from prophet import Prophet
import joblib

def handler(event, context):
    dados = pd.read_csv('./data/dados.csv')
    dados.Data = pd.to_datetime(dados.Data, format="%d/%m/%Y")

    dados = dados.drop('Unnamed: 0', axis=1)
    dados.columns = ['ds', 'y']
    dados.y = pd.to_numeric(dados.y)
    dados = dados.sort_values('ds').reset_index()
    dados_prophet = dados.drop('index', axis=1)

    treino = dados.sample(frac=0.8, random_state=0)
    teste_prophet = dados.drop(treino.index)

    modelo = Prophet(daily_seasonality=True,
                               weekly_seasonality=True,
                               yearly_seasonality=False,
                               seasonality_mode = 'multiplicative')
    modelo.fit(treino)

    with open('./models/modelo.pkl', 'wb') as file:
        joblib.dump(modelo, file)

if __name__ == '__main__':
    handler(None,None)