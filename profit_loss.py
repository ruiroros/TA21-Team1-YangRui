from pathlib import Path
import csv, requests

# file path to the profit and loss csv file 
profitloss_fp = Path.cwd()/"csv_reports"/"profit-and-loss-usd.csv"
# empty list created for the values of profit and loss and days
profit_loss = []
days = []

def profitloss_function():
    """
    # the function is to access the data, and find the difference between the net profit between each days
    """

    # setting the csv file to access the data in read mode
    with profitloss_fp.open(mode='r', encoding='UTF-8', newline="") as file:
        # the csv file is being read 
        profitloss_read = csv.reader(file)
        # the headers are skipped and only the values are being read
        next(profitloss_read)

        # a for loop is created 
        for line in profitloss_read:
            # the net profit values are being assigned to a variable
            netprofit = line[4]
            # the net profit values are appended to the empty list created earlier
            profit_loss.append(netprofit)

            # the number of days are being assigned to a variable
            day = line[0]
            # the number of days are appended to the list for days created earlier
            days.append(day)

        # x acts as a counter 
        x = 1

        # a try statement is used to execute the code if there are no exceptions
        try:
            # while the counter is less than the number of items in the list appended
            while x < len(profit_loss):
                api_key = "0PXEE709XYMK7M42"
                url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"
                response = requests.get(url)
                info = response.json()
                forex = float(info['Realtime Currency Exchange Rate']['5. Exchange Rate'])

                difference = float(profit_loss[x]) - float(profit_loss[x-1])
                x += 1 
                if difference <= 0:
                    msg = f"[PROFIT DEFICIT] DAY: {days[x-1]}, AMOUNT: SGD{abs(difference*forex)}"

                else: 
                    continue
                return msg

            if difference > 0:
                msg = "[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"
                return msg

        except ValueError:
            print("Please enter an appropriate value according to the argument type.")

        except TypeError:
            print("Please apply an appropriate operation or function according to the object type.")


print(profitloss_function())
