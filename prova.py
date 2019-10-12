import csv
import pandas
import requests
import json

result = pandas.read_csv('llistaespecies.csv',sep='\t')
phylum=requests.get("http://api.gbif.org/v1/occurrence/search#Aves")
print(phylum.json())

#sespec=result.loc[: , "scientificName"] #sespec[0] retorna el nom de la especie com a string
#i = 0
#for row in result:
#	print(sespec[i])
#	i += 1
