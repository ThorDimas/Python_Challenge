import os
import csv

#create the path to the file
PyBank_path = os.path.join('Resources', 'budget_data.csv')

months = 0
prev_pnl = 0
month_of_change = []
pnl_change_list = []
great_incr_profit = ["", 0]
great_decr_prof = ["", 99999999999999999]
profit_losses = 0


with open(PyBank_path) as bankfile:
    reader = csv.DictReader(bankfile)

    for row in reader:
        
        #track the totals
        months = months + 1
        profit_losses = profit_losses + int(row['Profit/Losses'])

        #track the revenue change
        change_in_pnl = int(row['Profit/Losses']) - prev_pnl
        prev_pnl = int(row['Profit/Losses'])
        pnl_change_list = pnl_change_list + [change_in_pnl]
        month_of_change = month_of_change + [row['Date']]

        #Calculate th greates increase
        if change_in_pnl > great_incr_profit[1]:
            great_incr_profit[0] = row['Date']
            great_incr_profit[1] = change_in_pnl

        #calculate the greates decrease
        if change_in_pnl < great_decr_prof[1]:
            great_decr_prof[0] = row['Date']
            great_decr_prof[1] = change_in_pnl

#calculate the average revenue change
pnl_average = sum(pnl_change_list) /len(pnl_change_list)

#print the results
print(
f'Financial Analysis\n'
f'--------------------------\n'
f'Total Months: {months}\n'
f'Total: ${profit_losses}\n'
f'Average Change: ${pnl_average}\n'
f'Greatest Increase in Profits: {great_incr_profit}'
f'Greatest Decrease in Profits: {great_decr_prof}'    
)

