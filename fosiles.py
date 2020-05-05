#Este programa busca hace una lista con los fósiles del 
#juego de animal crossing.

import requests
from bs4 import BeautifulSoup

URL = "https://animalcrossing.fandom.com/wiki/Fossils_(New_Horizons)"

res = requests.get(URL).text
soup = BeautifulSoup(res,'html.parser')
tablas = soup.find_all('table', class_="sortable")

for items in tablas[:-1]:
    #fosiles1 guarda los fósiles de una sola pieza
    fosiles1 = [' '.join(item.text.split()) for item in items.find_all(['a'])]
   
for items in tablas:
    #en fosiles2 van los fósiles con más de una pieza 
    fosiles2 = [' '.join(item.text.split()) for item in items.find_all(['a'])]

