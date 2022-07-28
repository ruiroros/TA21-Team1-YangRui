import csv
from pathlib import Path
fp = Path.cwd()
overheads_fp = fp/"csv_reports"/"overheads-45.csv"

print(fp)
print(overheads_fp)

with overheads_fp.open(mode='r', encoding='UTF-8') as file:
    overheads_read = file.read()

print(overheads_read)

