from pathlib import Path
import csv

coh_fp = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv" 

def cash_on_hand_function():
    cash_on_hand = []

    with coh_fp.open(mode='r', encoding='UTF-8', newline="") as file:
        cash_read = csv.reader(file)
        next(cash_read)
        
        for line in cash_read:
            coh = line[1]
            cash_on_hand.append(coh)

        x = 1
        diff = []
        while x < 10:
            difference = float(cash_on_hand[x]) - float(cash_on_hand[x-1])
            print(difference)
            diff.append(difference)
            diff.sort()
            x += 1
            if difference < 0:
                message = "test only"
            else:
                message = "ok"

        #wht tf is the return not working tf
        return message

cash_on_hand_function()



            # for days, ca`sh in enumerate(line):
            #     print(cash)
            # maybe use def function with return?

    #why tf got the days number!!! how to get rid pls
        #empty_list = []
        #for line in cash_read:
            #cash_on_hand = line[1]
            #empty_list.append(cash_on_hand)
