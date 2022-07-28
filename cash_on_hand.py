from pathlib import Path
# cwd now is np one drive/"IGP PFB"/"project_group"/"cash_on_hand.py"
fp = Path.cwd()
cash_fp = fp/"cash-on-hand-usd.csv"
print(cash_fp)
print(fp)
