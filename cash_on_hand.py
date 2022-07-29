from pathlib import Path
import csv

# cwd now is np one drive/"IGP PFB"/"project_group"/"cash_on_hand.py"
cash_fp = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"
# print(cash_fp)

with cash_fp.open(mode='r', encoding='UTF-8', newline="") as file:
    cash_read = csv.reader(file)
    next(cash_read)

empty_list = []
def diff_in_cash_values(final_value):
    for line in cash_read:
        cash_on_hand = int(line[1])
        empty_list.append(cash_on_hand)
    final_value = empty_list[0]-empty_list[1]
    print(final_value)
        # for days, ca`sh in enumerate(line):
        #     print(cash)
        # maybe use def function with return?

#why tf got the days number!!! how to get rid pls
    #empty_list = []
    #for line in cash_read:
        #cash_on_hand = line[1]
        #empty_list.append(cash_on_hand)
