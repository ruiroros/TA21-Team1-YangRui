from pathlib import Path
import csv
import requests, json

# empty list is created for the values of the overhead 
data = []
# empty dictionary  is created for the categories of the overheads
overheads = {}

# an API key is retrieved from AlphaVantage
api_key = "0PXEE709XYMK7M42"
# the url for the real time currency exchange rate is retrieved 
url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"
# the requests library and get method is used to call the API
response = requests.get(url)
# # retrieve data with .json from response and save it as data and assigned to a new variable
info = response.json()

def overhead_function():
    """
    the function is used to determine the highest overhead and the category is belongs to 
    """
    # a file path to the overheads csv file is created
    overheads_fp = Path.cwd()/"csv_reports"/"overheads-day-45.csv"

    # setting the csv file to access the data in read mode
    with overheads_fp.open(mode='r', encoding='UTF-8', newline="") as file:
        # the csv file is being read 
        overheads_reader = csv.reader(file)
        # the headers are skipped and only the values are being read
        next(overheads_reader)

        # a for loop is created 
        for line in overheads_reader:
            # the values of the overheads are identified and assigned to a new variable 
            value = float(line[1])
            # the overhead values are appended to the empty list created earlier
            data.append(value)

            # ???
            x = line[0]
            overheads[value] = x

        # API key is retrieved from AlphaVantage
        api_key = "0PXEE709XYMK7M42"
        # url for the real time currency exchange rate is retrieved 
        url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"
        # the requests library and get method is used to call the API
        response = requests.get(url)
        # retrieve data with .json from response and save it as data and assigned to a new variable
        info = response.json()
        # the data is converted into a float and assigned to a new variable
        forex = float(info['Realtime Currency Exchange Rate']['5. Exchange Rate'])

        # the max() method is used to determine the highest value among the overhead values
        highestdata = max(data)
        # the category of the highest overhead value is identified 
        highestcat = overheads[highestdata]
        # the message when the highest value is identified with the category is displayed
        msg = f"[HIGHEST OVERHEADS] {highestcat}: SGD{highestdata*forex}"
        # the message is printed
        print(msg)

# executes the function 
overhead_function()
