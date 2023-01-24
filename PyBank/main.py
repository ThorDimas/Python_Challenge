import os
import csv

#create the path to the file
PyBank_path = os.path.join('Resources', 'budget_data.csv')

months = 0
prev_pnl = 0
month_of_change = []
pnl_change_list = []
great_incr_profit = ["", 0]
great_decr_prof = ["", 9999999999]
profit_losses = 0


with open(PyBank_path) as bankfile:
    reader = csv.DictReader(bankfile)
    #Dictreader instead of reader to avoid using next for the first row. Use the name of the header
    for row in reader:        
        months = months + 1
        profit_losses = profit_losses + int(row['Profit/Losses'])

        #append and calculate the revenue change over each iteration of row
        change_in_pnl = int(row['Profit/Losses']) - prev_pnl
        prev_pnl = int(row['Profit/Losses'])
        pnl_change_list = pnl_change_list + [change_in_pnl]
        month_of_change = month_of_change + [row['Date']]

        #Calculate th greates increase. If the change in pnl is higher, then append the month and amount
        if change_in_pnl > great_incr_profit[1]:
            great_incr_profit[0] = row['Date']
            great_incr_profit[1] = change_in_pnl

        #same for decrease
        if change_in_pnl < great_decr_prof[1]:
            great_decr_prof[0] = row['Date']
            great_decr_prof[1] = change_in_pnl

#calculate the average revenue change
#Note that I tryed different approaches and still not sure why I'm getting a different result in the average change

pnl_change_list.pop(0)
total_change = sum(pnl_change_list)
total_months = months
pnl_average = total_change/total_months

# #print the results
results = (
f'Financial Analysis\n'
f'--------------------------\n'
f'Total Months: {months}\n'
f'Total: ${profit_losses}\n'
f'Average Change: ${pnl_average}\n'
f'Greatest Increase in Profits: {great_incr_profit[0]} (${great_incr_profit[1]})\n'
f'Greatest Decrease in Profits: {great_decr_prof[0]} (${great_decr_prof[1]})'    
)
print(results)

pybank_results = os.path.join('analysis', 'analysis.txt')

with open(pybank_results, "w") as results_file:
    results_file.write(results)


