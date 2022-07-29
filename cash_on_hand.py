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

# vanda : append to empty list?? enumerate and use re.search(pattern='[0-9][0-9][0-9][0-9][0-9][0-9][0-9]', string = index)/findall?

# rui starts from line 15 TRY 

cash_string = str(cash_read)
print(cash_string)
# print(type(cash_string))
print(cash_string[2])

