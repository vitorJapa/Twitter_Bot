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

emparedado1 = 'Barbara'
emparedado2 = 'Natalia'
emparedado3 = 'Arthur'
start_time = '2022-02-13T22:00:01Z'
end_time = '2022-02-15T22:00:01Z'

client = tw.Client(bearer_token=bearer_token, consumer_key=consumer_key, consumer_secret=consumer_secret_key, access_token=access_token, access_token_secret=secret_token)
base = []
total1 = 0
total2 = 0
total3 = 0
query = ('Fora ' + '%s')%(emparedado1)
busca1 = client.get_recent_tweets_count(query=query, start_time = start_time, end_time =end_time )
dados1 = busca1.data
for i in dados1:
    count1 = i['tweet_count']
    total1 = total1 + count1
#print(total1)

query = ('Fora ' + '%s')%(emparedado2)
busca2 = client.get_recent_tweets_count(query=query, start_time = start_time, end_time =end_time )
dados2 = busca2.data
for i in dados2:
    count2 = i['tweet_count']
    total2 = total2 + count2
#print(total2)

query = ('Fora ' + '%s')%(emparedado3)
busca3 = client.get_recent_tweets_count(query=query, start_time = start_time, end_time =end_time )
dados3 = busca3.data
for i in dados3:
    count3 = i['tweet_count']
    total3 = total3 + count3
#print(total3)

linha = [0 for j in range(4)]
linha[0] = total1 + total2 + total3
linha[1] = total1
linha[2] = total2
linha[3] = total3
base.append(linha)
baseBBB = pd.DataFrame(base)
baseBBB.columns = ['Total Votos', emparedado1, emparedado2, emparedado3]
baseView = baseBBB.drop(['Total Votos'], axis=1)
comentarios = baseView.sum().sort_values(ascending=False).to_list()
participantes = baseView.sum().sort_values(ascending=False).index.to_list()
base2 = pd.DataFrame(zip(participantes,comentarios))
base2.columns = ['Participantes', 'Votos de Fora']
total_tweets = base2['Votos de Fora'].sum()
base2['Porcentagem'] = base2['Votos de Fora']/total_tweets
base2['Porcentagem'] = base2['Porcentagem'].map("{:1%}".format)
print(base2[['Participantes', 'Votos de Fora', 'Porcentagem']])
