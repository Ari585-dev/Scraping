from bs4 import BeautifulSoup
import requests
import pandas as pd
from IPython.display import display, HTML





def scrp1 () :
    url ='https://www.gamerscolombia.com/tienda?productCategories[]=8' 
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    name = soup.find_all('h3', class_='product-title')
    nombres=list()

    for i in name:
        
        nombres.append(i.text)

    #print(nombres)

    price = soup.find_all('h4', class_='product-price col-12')
    precios=list()

    for i in price:
        
        precios.append(i.text)

    #print(precios)
    tam= len(nombres)
    tam2= len(precios)
    pd.set_option('display.max_rows', None)
    df = pd.DataFrame({'COMPUTADORA':nombres, 'PRECIO$':precios}, index=list(range(0,tam2)))
    print(df)

  #-----------------------------------------------------------------------------------------

def scrp2 () :
    url ='https://asyscomputadores.com/computadores-portatiles-gamers/' 
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    name = soup.find_all('h2', class_='woo-loop-product__title')
    nombres=list()

    for i in name:
        
        nombres.append(i.text)

    #print(nombres)

    price = soup.find_all('span', class_='woocommerce-Price-currencySymbol')
    precios=list()

    prices=[]
    
    price = soup.find_all('ins')
    for i in price:
        prices.append(str(i.text))
    #print(prices)
    
    tam = len(nombres)
    tam2 = len(prices)
    pd.set_option('display.max_rows', None)
    df = pd.DataFrame({'COMPUTADORA':nombres, 'PRECIO$':prices}, index=list(range(0,tam2)))
    
    print(df)
   
    


def scrp3 ():
    url ='https://www.panamericana.com.co/tecnologia/computadores-y-tablets/portatiles' 
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    name = soup.find_all('a', class_='item__showcase__productname__link')
    nombres=list()

    for i in name:
        
        nombres.append(i.text)

    #print(nombres)

    price = soup.find_all('span', class_='item__showcase__category__price-best showcase__price-best')
    precios=list()

    for i in price:
        
        precios.append(i.text)

    #print(precios)
    tam= len(nombres)
    tam2= len(precios)
    

    df = pd.DataFrame({'COMPUTADORA':nombres, 'PRECIO$':precios}, index=list(range(0,tam2)))
    print(df)  

