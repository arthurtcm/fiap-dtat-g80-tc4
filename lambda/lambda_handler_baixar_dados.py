
from bs4 import BeautifulSoup
import pandas as pd
import requests


def handler(event, context):
    url = 'http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        table = soup.find('table', {'id': 'grd_DXMainTable'})

        dados = pd.read_html(str(table),skiprows=0)[0]
        dados.columns = ['Data', 'Price']
        dados = dados.drop(0)
        
        dados.to_csv('./data/dados.csv')
        
    else:
        print('Falha ao acessar a página: Status Code', response.status_code)


if __name__ == '__main__':
    handler(None,None)