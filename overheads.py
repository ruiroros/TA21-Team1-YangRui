import csv
from pathlib import Path

overheads_fp = Path.cwd()/"csv_reports"/"overheads-day-45.csv"

def overheads_function():
    category = []
    overheads = []

    with overheads_fp.open(mode='r', encoding='UTF-8', newline='') as file:
        overheads_read = csv.reader(file)
        next(overheads_read)
        
        for line in overheads_read:
            cat = line[0]
            category.append(cat)

            ovheads = float(line[1])
            overheads.append(ovheads)

        highestcat = max(category)
        highestoverheads = overheads[highestcat]

        message = '[HIGHEST OVERHEADS] {highestoverheads.upper}: SGD{highestcat}'
        print(message)

overheads_function()

