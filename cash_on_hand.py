from pathlib import Path
import csv

coh_fp = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv" 

def cash_on_hand_function():
    cash_on_hand = []
    days = []

    with coh_fp.open(mode='r', encoding='UTF-8', newline="") as file:
        cash_read = csv.reader(file)
        next(cash_read)
        
        for line in cash_read:
            coh = line[1]
            cash_on_hand.append(coh)

            day = line[0]
            days.append(day)
        
        def loop():
            x = 1
            while x < len(cash_on_hand):
                difference = float(cash_on_hand[x]) - float(cash_on_hand[x-1])

                x += 1
                if difference <= 0:
                    #WRONG!!! NEED CONVERT DIFFERENCE FROM USD TO SGD BUT HOW 
                    message = f"[CASH DEFICIT] DAY:{days[x-1]}, AMOUNT: SGD{abs(difference)} "
                else: 
                    #should be ok? chck w teacher 
                    message = f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY "
                    
                print(message)
        loop()

cash_on_hand_function()
