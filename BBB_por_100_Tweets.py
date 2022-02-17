import tweepy as tw
import pandas as pd
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

bearer_token = os.environ.get("bearer_token")
consumer_key = os.environ.get("consumer_key")
consumer_secret_key = os.environ.get("consumer_secret_key")
access_token = os.environ.get("access_token")
secret_token = os.environ.get("secret_token")

client = tw.Client(bearer_token=bearer_token, consumer_key=consumer_key, consumer_secret=consumer_secret_key, access_token=access_token, access_token_secret=secret_token)

busca = client.search_recent_tweets(query='BBB', max_results = 100)
dados = busca.data
base = []
for i in dados:
    linha = [0 for j in range(19)]
    linha[0] = i.text
    texto = i.text
    if ('RT' in texto):
        posicao = texto.find(':')
        texto = texto[posicao+2:]
        linha[18] = 1

    linha[1] = 1 if ('lais caldas' in texto.lower() or 'lais' in texto.lower()) else 0
    linha[2] = 1 if ('jessilane' in texto.lower() or 'jessi' in texto.lower()) else 0
    linha[3] = 1 if ('eliezer' in texto.lower() or 'eli' in texto.lower()) else 0
    linha[4] = 1 if ('eslovenia' in texto.lower() or 'eslo' in texto.lower()) else 0
    linha[5] = 1 if ('lucas' in texto.lower() or 'piscadinha' in texto.lower()) else 0
    linha[6] = 1 if ('arthur aguiar' in texto.lower() or 'arthur' in texto.lower()) else 0
    linha[7] = 1 if ('natalia' in texto.lower() or 'nath' in texto.lower()) else 0
    linha[8] = 1 if ('vinicius' in texto.lower() or 'viny' in texto.lower()) else 0
    linha[9] = 1 if ('pedro scooby' in texto.lower() or 'scooby' in texto.lower() or 'pedro' in texto.lower()) else 0
    linha[10] = 1 if ('brunna' in texto.lower() or 'brudimila' in texto.lower()) else 0
    linha[11] = 1 if ('paulo andre' in texto.lower() or 'pa' in texto.lower()) else 0
    linha[12] = 1 if ('jade picon' in texto.lower() or 'jade' in texto.lower() or 'piton' in texto.lower()) else 0
    linha[13] = 1 if ('douglas silva' in texto.lower() or 'dg' in texto.lower() or 'douglas' in texto.lower()) else 0
    linha[14] = 1 if ('linn da quebrada' in texto.lower() or 'lina' in texto.lower() or 'linna' in texto.lower()) else 0
    linha[15] = 1 if ('tiago abravanel' in texto.lower() or 'tiago' in texto.lower() or 'abravanel' in texto.lower()) else 0
    linha[16] = 1 if ('larissa' in texto.lower() or 'lari' in texto.lower()) else 0
    linha[17] = 1 if ('gustavo' in texto.lower()) else 0



    base.append(linha)

baseBBB = pd.DataFrame(base)
baseBBB.columns = ['texto', 'Lais', 'Jessi', 'Eli', 'Eslovenia', 'Lucas', 'Arthur Aguiar', 'Natalia', 'Vinicius', 'Scooby', 'Brunna', 'Pa', 'Jade', 'DG', 'Linna', 'Tiago', 'Larissa', 'Gustavo', 'RT']
##print(baseBBB.sum())
baseView = baseBBB.drop(['texto', 'RT'], axis=1)
#print(baseView.sum().sort_values(ascending=False))
comentarios = baseView.sum().sort_values(ascending=False).to_list()
participantes = baseView.sum().sort_values(ascending=False).index.to_list()

base2 = pd.DataFrame(zip(participantes,comentarios))
base2.columns = ['Participantes', 'Tweets']
total_comentarios = base2['Tweets'].sum()
base2['perc'] = base2['Tweets']/total_comentarios
base2['perc_form'] = base2['perc'].map("{:1%}".format)
print(base2[['Participantes', 'Tweets', 'perc_form']])
