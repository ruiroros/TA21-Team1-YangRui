import api, cash_on_hand, overheads, profit_loss
from pathlib import Path

def main_function():
    fp = Path.cwd()/'summary_report.txt'
    fp.touch()

    api.api_function()
    overheads.overhead_function()
    cash_on_hand.coh_function()
    profit_loss.profitloss_function()

main_function()

