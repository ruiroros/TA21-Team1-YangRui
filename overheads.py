from pathlib import Path
import csv

data = []
overheads = {}

def overhead_function():

    overheads_fp = Path.cwd()/"csv_reports"/"overheads-day-45.csv"
    with overheads_fp.open(mode='r', encoding='UTF-8', newline="") as file:
        overheads_reader = csv.reader(file)
        next(overheads_reader)

        for line in overheads_reader: 
            value = float(line[1])
            data.append(value)

            x = line[0]
            overheads[value] = x

        highestdata = max(data)
        highestcat = overheads[highestdata]
        msg = f"[HIGHEST OVERHEADS] {highestcat}: SGD{highestdata}"
        return(msg)

print(overhead_function())