import requests
from pathlib import Path


api_key = "0PXEE709XYMK7M42"
url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"
response = requests.get(url)
data = response.json()

def api_function():
    forex = float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])

    exchange_rate = f'[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{forex}'
    print(exchange_rate)


    
api_function()