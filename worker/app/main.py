
import requests
import pandas as pd

B3_URL = "https://sistemasweb.b3.com.br/PlantaoNoticias/Noticias/ListarTitulosNoticiasInicial?agencia=18"
API_URL = "http://b3newsapi/bulk_news"

def load_data():
    response = requests.get(B3_URL)
    response = [record['NwsMsg'] for record in response.json()]
    df = pd.json_normalize(response)
    df = apply_calculation(df) # optional, if creating new columns here need to add them in the API as well
    #add new columns to response before sending to POST

    x = requests.post(API_URL, json = response)
    print(x)

# in case you need aditional proccessing
def apply_calculation(df):
    return df

if __name__ == "__main__":
    load_data()