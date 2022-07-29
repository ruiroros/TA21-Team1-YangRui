from pathlib import Path
# cwd now is np one drive/"IGP PFB"/"project_group"/"cash_on_hand.py"
fp = Path.cwd()
cash_fp = fp/"csv_reports"/"cash-on-hand-usd.csv"
print(cash_fp)

with cash_fp.open(mode='r', encoding='UTF-8') as file:
    cash_read = file.read()

print(cash_read)

# vanda : append to empty list?? enumerate and use re.search(pattern='[0-9][0-9][0-9][0-9][0-9][0-9][0-9]', string = index)/findall?

# rui starts from line 15 TRY 

cash_string = str(cash_read)
print(cash_string)
# print(type(cash_string))
print(cash_string[2])

