from pathlib import Path
import csv
from pickle import APPEND

# cwd now is np one drive/"IGP PFB"/"project_group"/"cash_on_hand.py"
cash_fp = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"
# print(cash_fp)

with cash_fp.open(mode='r', encoding='UTF-8', newline="") as file:
    cash_read = csv.reader(file)
    next(cash_read)

    for line in cash_read:
        cash_on_hand = []
        cash_on_hand.append(float(line[1]))
        print(cash_on_hand)

#why tf got the days number!!! how to get rid pls

