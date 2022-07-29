from pathlib import Path
import csv 

profitloss_fp = Path.cwd/"csv_reports"/"profit-and-loss-usd.csv"

with profitloss_fp.open(mode='r', encoding='UTF-8') as file:
    profitloss_read = file.read()
    next(profitloss_read)

    for line in profitloss_read:
        profitloss = line[]
        print()

print(profitloss_read)

