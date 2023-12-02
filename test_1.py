import time
import requests
from bs4 import BeautifulSoup

stock = ['1101', '2330', '1584']

for i in range(len(stock)):
    r = requests.get("https://tw.stock.yahoo.com/quote/" + stock[i] + ".TW")
    soup = BeautifulSoup(r.text, 'html.parser')

    price = soup.find(
        'span', class_=['Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)',
                        'Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)',
                        'Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)'])

    if (price == None):
        r = requests.get(
            "https://tw.stock.yahoo.com/quote/" + stock[i] + ".TWO")
        soup = BeautifulSoup(r.text, 'html.parser')

        price = soup.find(
            'span', class_=['Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)',
                            'Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)',
                            'Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)'])

    message = "股票: " + stock[i] + " 的價格為: " + price.get_text()
    chat_id = '6570702631'
    token = '6802588978:AAGhZDjKi9oVG228ICRrqjwLBj9dE5yTNgI'
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"

    requests.get(url)
    time.sleep(3)
