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

        x = 1
        for difference in profit_loss:
            difference = float(profit_loss[x]) - float(profit_loss[x-1])

            x += 1 
            if difference <= 0:
                message = "deficit"

            else:
                message = "na"

            print(message)

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

