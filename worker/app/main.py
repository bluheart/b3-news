import requests
import pandas as pd
import json

B3_URL = "https://sistemasweb.b3.com.br/PlantaoNoticias/Noticias/ListarTitulosNoticiasInicial?agencia=18"
API_URL = "http://b3newsapi/bulk_news"

def load_data():
    response = requests.get(B3_URL)
    response = [record['NwsMsg'] for record in response.json()]
    df = pd.json_normalize(response)
    df['prob'] = 0
    df['status'] = ''
    df['treated'] = False
    result = df.to_json(orient="records")
    result = json.loads(result)
    for record in result:
        record['headline'] = record['headline'].replace('\\', '')
    x = requests.post(API_URL, json = result)

# in case you need aditional proccessing
def apply_calculation(df):
    return df

if __name__ == "__main__":
    load_data()