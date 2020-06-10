from pymongo import MongoClient
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

### funcoes auxiliares ###
def pegarVitorias(linha):
    for x in range(len(linha)):
        if (linha)[x]=='-':
            return int((linha)[x-2] +(linha)[x-1])
            #return linha[x-1]

f = open('settings.txt', 'r')

MONGO_URI = f.readline()
#print(MONGO_URI)
client = MongoClient(MONGO_URI)
db = client['ufcData']
fighters = db['manBantamWeight']

p = (fighters.find()) #cursor
toDf = []
for x in p:
    x['wins'] = pegarVitorias(x['category_position'])
    toDf.append(x)
#    print(x)

df = pd.DataFrame(toDf)
df.drop('_id', axis=1, inplace=True)
df.drop('category_position', axis=1, inplace=True)
df.drop('nickname', axis=1, inplace=True)
print(df)
#print(df.describe()) #estatisticas sobre os lutadores

client.close()
#disconnect() #desconectando do banco
