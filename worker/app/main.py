
import requests

b3url = "https://sistemasweb.b3.com.br/PlantaoNoticias/Noticias/ListarTitulosNoticias?agencia=18&palavra=&dataInicial=2022-11-01&dataFinal=2022-11-01"
url = "http://b3newsapi/bulk_news"

response = requests.get(b3url)

response = [record['NwsMsg'] for record in response.json()]
x = requests.post(url, json = response)