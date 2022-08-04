from pathlib import Path
import csv, api

data = []
overheads = {}

def overhead_function():
    overheads_fp = Path.cwd()/"csv_reports"/"overheads-day-45.csv"
    # summaryfp = Path.cwd()/'summary_report.txt'

    with overheads_fp.open(mode='r', encoding='UTF-8', newline="") as file:
        overheads_reader = csv.reader(file)
        next(overheads_reader)

        for line in overheads_reader: 
            value = float(line[1])
            data.append(value)

            x = line[0]
            overheads[value] = x

            
        y = forex
        highestdata = max(data)
        highestcat = overheads[highestdata]
        msg = f"[HIGHEST OVERHEADS] {highestcat}: SGD{highestdata*y}"


        # with summaryfp.open(mode='a', encoding='UTF-8', newline= '') as file: 
        #     file.writelines(f"\n{msg}")

        return msg


print(overhead_function())
