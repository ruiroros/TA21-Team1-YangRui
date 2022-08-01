import csv 
from pathlib import Path
from unicodedata import category

fp = Path.cwd()
print(fp)
overheads_fp = fp/"csv_reports"/"overheads-day-45.csv"

def overheads_function():
    category_list = []
    overheads_list = []

    with overheads_fp.open(mode='r', encoding='UTF-8', newline="") as file:
        overheads_read = csv.reader(file)
        print(next(overheads_read))

        for line in overheads_read:
            category = line[0]
            overheads = line[1]
            category_list.append(category)
            overheads_list.append(overheads)
    print(type(category_list))
    print(type(overheads_list))
    # *lists are iterable
    # use max() function?

print(overheads_function())