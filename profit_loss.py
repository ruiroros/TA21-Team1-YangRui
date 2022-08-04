from pathlib import Path
import csv, requests

# file path to the profit and loss csv file 
profitloss_fp = Path.cwd()/"csv_reports"/"profit-and-loss-usd.csv"
# empty list created for the values of net profit 
profit_loss = []
# empty list created for the day numbers 
days = []

def profitloss_function():
    """
    the function is to access the data, and find the difference between the net profit between each days
    """

    fp = Path.cwd()/'summary_report.txt'
    fp.touch()

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

            # the day numbers are being assigned to a variable
            day = line[0]
            # the day numbers are appended to the list for days created earlier
            days.append(day)

        with fp.open(mode='a', encoding='UTF-8', newline= '') as file:

        # x acts as a counter 
            x = 1
            # a try statement is used to execute the code if there are no exceptions
            try:
                # while the counter is less than the number of items in the list appended
                while x < len(profit_loss):
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


                    # the difference between net profits are calculated using the counter 
                    difference = float(profit_loss[x]) - float(profit_loss[x-1])
                    # 1 is added to the counter and looped
                    x += 1 
                    # if statement with comparion operator
                    if difference <= 0:
                        # if the condition is met, the message will be displayed 
                        msg = f"[PROFIT DEFICIT] DAY: {days[x-1]}, AMOUNT: SGD{abs(difference*forex)}"

                    # the second statement is executed if the conditions in the if statement are not met
                    else: 
                        # the program continues to calculate the difference in net profits until conditions of the if statement are not met 
                        continue
                    # return keyword returns the display message
                    return(msg)


                # if statement with comparion operator
                if difference > 0:
                    # if the condition is met the message in the f string will be displayed
                    msg = "[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"
                    # return keyword returns the display message
                
                #code dosent append we are sorry we tried until the last minute, but our main.py able to execute
                    return(msg)

                with fp.open(mode='a', encoding='UTF-8', newline= '') as file:
                    file.write(f"\n{msg}")

            # except statement will execute with ValueError when try statement fails
            except ValueError:
                # the code will print the message when the try statement fails 
                print("Please enter an appropriate value according to the argument type.")

            # except statement will execute with TypeError when try statement fails
            except TypeError:
                # the code will print the message when the try statement fails 
                print("Please apply an appropriate operation or function according to the object type.")


# executes the function 
print(profitloss_function())