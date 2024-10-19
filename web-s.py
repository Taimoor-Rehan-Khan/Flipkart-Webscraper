from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd

service = Service("C:/Users/fires/chromedriver/win64-132.0.6779.0/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("https://www.flipkart.com/search?sid=b5g&otracker=CLP_Filters&p%5B%5D=facets.brand%255B%255D%3DHP&p%5B%5D=facets.brand%255B%255D%3DASUS&p%5B%5D=facets.brand%255B%255D%3DLenovo")

content = driver.page_source
soup = BeautifulSoup(content, "html.parser")

for a in soup.findAll('div', attrs={'class':'NqpwHC'}): 
    name = str(a)
    name = name.split("<div class=\"NqpwHC\">")
    name = name[1]
    name = name.split("</div>")
    name = name[0]
    products.append(name)

for b in soup.findAll('div', attrs={'class':'Nx9bqj'}): 
    price = str(b)
    price = price.split("<div class=\"Nx9bqj\">")
    price = price[1]
    price = price.split("</div>")
    price = price[0]
    prices.append(price)

for c in soup.findAll('div', attrs={'class':'XQDdHH'}):
    rating = str(c)
    rating = rating.split("<div class=\"XQDdHH\">")
    rating = rating[1]
    rating = rating.split("<img class=\"Rza2QY\" src=\"data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==\"/></div>")
    rating = rating[0]
    ratings.append(rating)

df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings})
df.to_csv('C:/Users/fires/Desktop/FSU/Y2 S1/CSCI 200/products.csv', index=False, encoding='utf-8')