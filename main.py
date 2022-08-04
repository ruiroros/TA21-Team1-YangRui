import api, coh, overheads, profit_loss
from pathlib import Path

def main_function():
    fp = Path.cwd()/'summary_report.txt'
    fp.touch()
    
    # forex = api.api_function()
    # one = overheads.overhead_function()
    # two = coh.coh_function()
    # thr = profit_loss.profitloss_function()

    forex = api.api_function()
    one = overheads.overhead_function()
    two = coh.coh_function()
    thr = profit_loss.profitloss_function()



    # with fp.open(mode='w', encoding='UTF-8', newline= '') as file:
    #     file.writelines(forex)
    # with fp.open(mode='a', encoding='UTF-8', newline= '') as file:
    #     file.writelines(f"{one}")
    #     file.writelines(f"{two}")
    #     file.writelines(f"{thr}")
main_function()

