from pathlib import Path
import csv

# cwd now is np one drive/"IGP PFB"/"project_group"/"cash_on_hand.py"
cash_fp = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"
# print(cash_fp)

with cash_fp.open(mode='r', encoding='UTF-8', newline="") as file:
    cash_read = csv.reader(file)
    next(cash_read)

    for line in cash_read:
        print(line)

    cash_emptylist = []
    for sublist in line:
        cash_emptylist.append(sublist[1])
    
    print(cash_emptylist)


