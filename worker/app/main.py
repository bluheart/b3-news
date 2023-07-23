
import requests

b3url = "https://sistemasweb.b3.com.br/PlantaoNoticias/Noticias/ListarTitulosNoticias?agencia=18"
url = "http://b3newsapi/bulk_news"

response = requests.get(b3url)

response = [record['NwsMsg'] for record in response.json()]
x = requests.post(url, json = response)