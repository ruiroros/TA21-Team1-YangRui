from pathlib import Path
import csv 

profitloss_fp = Path.cwd()/"csv_reports"/"profit-and-loss-usd.csv"

def profitloss_function():
    profit_loss = []
    days = []

    with profitloss_fp.open(mode='r', encoding='UTF-8', newline="") as file:
        profitloss_read = csv.reader(file)
        next(profitloss_read)

        for line in profitloss_read:
            netprofit = line[4]
            profit_loss.append(netprofit)

            day = line[0]
            days.append(day)

        x = 1

        try:
            while x < len(profit_loss):
                difference = float(profit_loss[x]) - float(profit_loss[x-1])
                x += 1 
                if difference <= 0:
                    message = f"[PROFIT DEFICIT] DAY: {days[x-1]}, AMOUNT: SGD{abs(difference)}"

                else: 
                    continue
                return message

            if difference > 0:
                message = "[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"
                return message

        except ValueError:
            print("Please enter an appropriate value according to the argument type.")

        except TypeError:
            print("Please apply an appropriate operation or function according to the object type.")


print(profitloss_function())
