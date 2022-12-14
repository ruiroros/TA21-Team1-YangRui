import requests, json
from pathlib import Path

def api_function():
    """
    the function is to call the API and access the real time exchange rate data
    """
    fp = Path.cwd()/'summary_report.txt'
    fp.touch()

    # API key is retrieved from AlphaVantage
    api_key = "0PXEE709XYMK7M42"
    # url for the real time currency exchange rate is retrieved 
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"
    # the requests library and get method is used to call the API
    response = requests.get(url)
    # retrieve data with .json from response and save it as data and assigned to a new variable
    data = response.json()
    # the data is converted into a float and assigned to a new variable
    forex = float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
    from_symbol = (data['Realtime Currency Exchange Rate']['1. From_Currency Code'])
    to_symbol = (data['Realtime Currency Exchange Rate']['3. To_Currency Code'])

    # the data is displayed in a message using f string 
    exchange_rate = f'[REAL TIME CURRENCY CONVERSION RATE] {from_symbol}1 = {to_symbol}{forex}'
    # the message is printed
    print(exchange_rate)

    # writing to the summary report 
    with fp.open(mode='w', encoding='UTF-8', newline= '') as file:
        file.writelines(exchange_rate)

# executes the function
api_function()

