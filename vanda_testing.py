import csv
from pathlib import Path

fp = Path.cwd()
print(fp)
overheads_fp = fp/"csv_reports"/"overheads-day-45.csv"

def overheads_function():

    with overheads_fp.open(mode='r', encoding='UTF-8', newline="") as file:
        overheads_read = csv.reader(file)
        print(next(overheads_read))

        category_list = []
        overheads_list = []
        for line in overheads_read:
            category = line[0]
            overheads = line[1]
            category_list.append(category)
            overheads_list.append(overheads)
            print(category_list)
            print(overheads_list)
            # print(max(overheads_list))

    # *lists are iterable
    # use max() function?
    # use enumerate function?
    # handle exceptions using try, except, else
overheads_function()