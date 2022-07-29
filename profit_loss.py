from pathlib import Path
import csv 

profitloss_fp = Path.cwd/"csv_reports"/"profit-and-loss-usd.csv"

with profitloss_fp.open(mode='r', encoding='UTF-8', newline="") as file:
    profitloss_read = csv.reader(file)
    next(profitloss_read)

    for line in profitloss_read:
        profitloss = line[5]
        print(line[5])

####
# with cash_fp.open(mode='r', encoding='UTF-8', newline="") as file:
#     cash_read = csv.reader(file)
#     next(cash_read)

#     for line in cash_read:
#         cash_on_hand = line[1]
#         print(type(cash_on_hand))

