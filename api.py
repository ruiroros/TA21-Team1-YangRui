import requests, json
from pathlib import Path

api_key = "0PXEE709XYMK7M42"
url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"
response = requests.get(url)
data = response.json()

def forex1():

    api_key = "0PXEE709XYMK7M42"
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"
    response = requests.get(url)
    data = response.json()

    # summaryfp = Path.cwd()/'summary_report.txt'
    forex = float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
    return forex
    # exchange_rate = f'[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{forex}'
    # print(exchange_rate)

    # with summaryfp.open(mode='w', encoding='UTF-8', newline= '') as file: 
    #     file.writelines(exchange_rate)


print(forex1())