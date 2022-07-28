import csv
from pathlib import Path
fp = Path.cwd()
profitloss_fp = fp/"csv_reports"/"profit-and-loss-usd.csv"

print(fp)
print(profitloss_fp)

with profitloss_fp.open(mode='r', encoding='UTF-8') as file:
    profitloss_read = file.read()

print(profitloss_read)