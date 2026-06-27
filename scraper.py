import requests
from bs4 import BeautifulSoup
from config import headers, url

def scrape():
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    name = soup.find_all(class_="LineClampText__Wrapper-sc-277a5185-0 kzJsUD parts__ProductName-sc-7632c90a-7 fvTWHq")[0].get_text()
    price = soup.find_all(class_="parts__ScreenReaderPrice-sc-fd70cef5-6 dCVjrv")[0].get_text()
    price_before = soup.find_all(class_="parts__ScreenReaderPrice-sc-fd70cef5-6 dCVjrv")[1].get_text()
    remaining: int = soup.find_all(class_="parts__NumberToAnimate-sc-8607a6e4-0 jeWUmb")[0].get_text()
    sold: int = soup.find_all(class_="parts__NumberToAnimate-sc-8607a6e4-0 jeWUmb")[3].get_text()
    
    #print(f"{name}\n{price}\n{price_before}\nPozostało: {remaining}\nSprzedano: {sold}")
    return {
        "name": name,
        "actual_price": price,
        "price_before": price_before,
        "remaining": remaining,
        "sold": sold,
        "percentage_of_sales": int(sold) / (int(sold) + int(remaining)) * 100
    }