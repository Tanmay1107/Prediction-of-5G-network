import requests
from bs4 import BeautifulSoup
import pandas as pd 


products=[]
ratings=[]

URL = "https://www.amazon.in/s?k=iphone&ref=nb_sb_noss_2"
r = requests.get(URL)

soup = BeautifulSoup(r.content,'html5lib')

for a in soup.findAll('a',href=True, attrs={'class':'_4ddWXP'}):
 name=a.find('a', attrs={'class':'s1Q9rs'})
 rating=a.find('div', attrs={'class':'_30jeq3'})
 products.append(name.text)
 ratings.append(rating.text) 

df = pd.DataFrame({'Produnt Name':products,'Rating':ratings})
df.to_csv('product1.csv',index=False,encoding='utf-8') 