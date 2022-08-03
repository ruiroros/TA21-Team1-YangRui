import api, coh, overheads, profit_loss
from pathlib import Path

def main():
    fp = Path.cwd()/'summary_report.txt'
    fp.touch()
    
    forex = api.api_function()
    one = overheads.overhead_function(forex)
    two = coh.coh_function(forex)
    thr = profit_loss.profitloss_function(forex)

    with fp.open(mode='w', encoding='UTF-8', newline= '') as file:
        file.writelines(forex)
    with fp.open(mode='a', encoding='UTF-8', newline= '') as file:
        file.writelines(one)
        file.writelines(two)
        file.writelines(thr)


main()