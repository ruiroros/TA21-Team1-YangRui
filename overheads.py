from pathlib import Path
fp = Path.cwd()
overheads_fp = fp/"overheads-45.csv"

print(fp)
print(overheads_fp)

with overheads_fp.open(mode='r', encoding='UTF-8') as file:
    overheads_read = overheads_fp.read()

print(overheads_fp)

