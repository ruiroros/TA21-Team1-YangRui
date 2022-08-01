import requests
import csv 
from pathlib import Path

api_key = "0PXEE709XYMK7M42"
url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"

response = requests.get(url)
data = response.json()
print(data)

fp = Path.cwd()/"final_report.txt"

def api_function():
    pm25 = float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])

    exchange_rate = f'[CURRENCY CONVERSION RATE] USD1 = SGD{pm25}'

    if fp.exists():
        with fp.open(mode = 'w', encoding='UTF-8', newline="") as file:
            writer = csv.writer(file)

            writer.writerow(exchange_rate)
        return exchange_rate

api_function()