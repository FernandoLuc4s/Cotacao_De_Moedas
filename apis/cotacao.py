import requests
import json #pegar formato json
cotacoes = requests.get( "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()
cotacoes_dolar = cotacoes['USDBRL']['bid'] #pegar somente o bid do dolar
print(cotacoes_dolar) #pegando cotacao do dolar
