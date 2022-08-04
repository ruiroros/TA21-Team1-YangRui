from pathlib import Path
import csv, requests

# a file path to the cash on hand csv file is created
coh_fp = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv" 

def coh_function():
    """
    # the function is used to calculate the difference between the amount of cash between each day
    """

    fp = Path.cwd()/'summary_report.txt'
    fp.touch()
    
    # empty list is created for the cash values
    cash_on_hand = []
    # empty list is created for the day numbers
    days = []

    # setting the csv file to access the data in read mode
    with coh_fp.open(mode='r', encoding='UTF-8', newline="") as file:
        # the csv file is being read
        cash_read = csv.reader(file)
        # the headers are skipped and only the values are being read
        next(cash_read)
        
        # a for loop is created
        for line in cash_read:
            # the values of the cash on hand are identified and assigned to a new variable
            coh = line[1]
            # the values of the cash on hand are appended to the empty list created earlier
            cash_on_hand.append(coh)

            # the day numbers are being assigned to a variable
            day = line[0]
            # the day numbers are appended to the list for days created earlier
            days.append(day)
        
            # x acts as a counter
            x = 1
        
        # a try statement is used to execute the code if there are no exceptions
        try:
            # while the counter is less than the number of items in the list appended
            while x < len(cash_on_hand):
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

                # the difference between cash values are calculated using the counter 
                difference = float(cash_on_hand[x]) - float(cash_on_hand[x-1])
                # 1 is added to the counter and looped
                x += 1
                # if statement with comparion operator
                if difference <= 0:
                    # if the condition is met, the message will be displayed
                    message = f"[CASH DEFICIT] DAY: {days[x-1]}, AMOUNT: SGD{abs(difference*forex)} "

                # the second statement is executed if the conditions in the if statement are not met
                else:
                    # the program continues to calculate the difference in net profits until conditions of the if statement are not met 
                    continue 
                # return keyword returns the display message
                return message 

            # if statement with comparion operator
            if difference > 0:
                # if the condition is met the message in the f string will be displayed
                message = f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY "
                # return keyword returns the display message
                return message
                
        # except statement will execute with ValueError when try statement fails
        except ValueError:
            # the code will print the message when the try statement fails 
            print("Please enter an appropriate value according to the argument type.")
        
        # except statement will execute with TypeError when try statement fails
        except TypeError:
            # the code will print the message when the try statement fails
            print("Please apply an appropriate operation or function according to the object type.")

# executes the function 
print(coh_function())
