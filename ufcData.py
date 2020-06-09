from pymongo import MongoClient
from pathlib import Path
import pandas as pd

f = open('settings.txt', 'r')

MONGO_URI = f.readline()
#print(MONGO_URI)
client = MongoClient(MONGO_URI)
db = client['ufcData']
manBantamWeight = db['manBantamWeight']

p = (manBantamWeight.find()) #cursor
#for x in p:
#    print(x)

df = pd.DataFrame(list(p))

client.close()
#disconnect() #desconectando do banco
