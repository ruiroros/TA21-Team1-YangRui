import api, coh, overheads, profit_loss
from pathlib import Path

def main_function():
    fp = Path.cwd()/'summary_report.txt'
    fp.touch()
    
    forex = api.api_function()
    one = overheads.overhead_function()
    two = coh.coh_function()
    thr = profit_loss.profitloss_function()


    # with fp.open(mode='w', encoding='UTF-8', newline= '') as file:
    #     file.writelines(api.api_function())
    with fp.open(mode='w', encoding='UTF-8', newline= '') as file:
        file.writelines(f"\n {one}")
    with fp.open(mode='a', encoding='UTF-8', newline= '') as file:
        file.writelines(f"\n {two}")
    with fp.open(mode='a', encoding='UTF-8', newline= '') as file:
        file.writelines(f"\n {thr}")
main_function()

# a = main_function()
# fp = Path.cwd()/'summary_report.txt'
# fp.touch()

# with fp.open(mode='w', encoding='UTF-8', newline= '') as file:
#     file.writelines(a)
    
