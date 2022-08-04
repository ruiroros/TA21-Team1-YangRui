from pathlib import Path
import csv
import requests, json

data = []
overheads = {}

api_key = "0PXEE709XYMK7M42"
url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"
response = requests.get(url)
info = response.json()


def overhead_function():
    overheads_fp = Path.cwd()/"csv_reports"/"overheads-day-45.csv"

    with overheads_fp.open(mode='r', encoding='UTF-8', newline="") as file:
        overheads_reader = csv.reader(file)
        next(overheads_reader)

        for line in overheads_reader: 
            value = float(line[1])
            data.append(value)

            x = line[0]
            overheads[value] = x

            # highestdata = max(data)
            # highestcat = overheads[highestdata]
            # msg = f"[HIGHEST OVERHEADS] {highestcat}: SGD{highestdata*y}"
            # print(msg)
        api_key = "0PXEE709XYMK7M42"
        url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"
        response = requests.get(url)
        info = response.json()
        forex = float(info['Realtime Currency Exchange Rate']['5. Exchange Rate'])

        highestdata = max(data)
        highestcat = overheads[highestdata]
        msg = f"[HIGHEST OVERHEADS] {highestcat}: SGD{highestdata*forex}"
        print(msg)


overhead_function()
