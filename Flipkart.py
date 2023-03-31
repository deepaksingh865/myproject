import requests
from bs4 import BeautifulSoup
import pandas as pd

washing_machine=[]
description=[]
price=[]


url="https://www.flipkart.com/search?q=washing+machine+under+5000&sid=j9e%2Cabm%2C8qx&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_27_sc_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_27_sc_na_na&as-pos=1&as-type=RECENT&suggestionId=washing+machine+under+5000%7CWashing+Machines&requestId=1d39478b-126a-4ba4-a8df-0515e6c1f0aa&as-searchtext=washing%20machine%20under%2050000"

for y in range(1,38):
    n_url = url + "&page" + str(y)     #*****Next Button URL********
    r = requests.get(n_url)
    soup = BeautifulSoup(r.text, "html.parser")
    boxsoup=soup.find("div",class_="_1YokD2 _3Mn1Gg")

    name=boxsoup.findAll("div", class_="_4rR01T")
    for i in name:
        washing_machine.append(i.text)

    des=boxsoup.findAll("ul", class_="_1xgFaf")
    for i in des:
        description.append(i.text)

    p=boxsoup.findAll("div", class_="_30jeq3 _1_WHN1")
    for i in p:
        price.append(i.text)

df=pd.DataFrame({"washing_machine":washing_machine,"price":price,"Des":description})
df.to_csv("Washing.csv")
print(df.head())