from pathlib import Path
import csv
import requests, json

# empty list is created for the values of the overhead 
data = []
# empty list is created for the categories of the overheads
overheads = {}

# an API key is retrieved from AlphaVantage
api_key = "0PXEE709XYMK7M42"
# the url for the real time currency exchange rate is retrieved 
url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"
# *(brightspace 7.2.3)
response = requests.get(url)
# 
info = response.json()

def overhead_function():
    """
    """
    #
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
