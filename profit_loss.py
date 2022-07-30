from pathlib import Path
import csv 

profitloss_fp = Path.cwd()/"csv_reports"/"profit-and-loss-usd.csv"

def profit_loss_function():
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

        def loop():
            x = 1
            # i think the error is in this line but ???
            while x < len(profit_loss):
                difference = float(profit_loss[x]) - float(profit_loss[x-1])
                x += 1 
                if difference <= 0:
                    #NEED CONVERT DIFF TO SGD 
                    message = f"[PROFIT DEFICIT] DAY: {days[x-1]}, AMOUNT: SGD{abs(difference)}"

                else:
                    message = "[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"

                print(message)
        loop()

profit_loss_function()


        # dont delete first might need
        # for line in profitloss:
        #     number = line[2]
        #     print(number)


####
# with cash_fp.open(mode='r', encoding='UTF-8', newline="") as file:
#     cash_read = csv.reader(file)
#     next(cash_read)

#     for line in cash_read:
#         cash_on_hand = line[1]
#         print(type(cash_on_hand))

