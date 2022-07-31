import csv
from pathlib import Path

overheads_fp = Path.cwd()/"csv_reports"/"overheads-day-45.csv"

def overheads_function():
    category = []
    overheads = []

    with overheads_fp.open(mode='r', encoding='UTF-8', newline='') as file:
        overheads_read = csv.reader(file)
        next(overheads_read)
        print(overheads_read)

        for line in overheads_read:
            cat = line[0]
            category.append(cat)

            ovheads = line[1]
            overheads.append(ovheads)
            




overheads_function()
