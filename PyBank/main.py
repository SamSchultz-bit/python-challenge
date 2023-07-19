import csv


budget = csv.reader(open('PyBank/Resources/budget_data.csv'))
header = next(budget)

months = 0
dollars = 0
change = 0 
tot_cha = 0
prev = 0
first = 1
inc_num = 0
dec_num = 0

for row in budget:
    months += 1
    dollars += int(row[1])

    if(first == 1):
        prev = int(row[1])
        first = 0

    change = int(row[1]) - prev
    prev = int(row[1])
    tot_cha += change

    if change > inc_num:
        inc_mon = row[0]
        inc_num = change

    elif change < dec_num:
        dec_mon = row[0]
        dec_num = change

avg = tot_cha / (months - 1)
avg = round(avg, 2)

output = (f''' 
      Financial Analysis
      ----------------------------
      Total Months: {months}
      Total: ${dollars}
      Average Change: ${avg}
      Greatest Increase in Profits: {inc_mon} (${inc_num})
      Greatest Decrease in Profits: {dec_mon} (${dec_num})
      ''')

print(output)

with open("PyBank/Analysis/budget_analysis.txt", 'w') as file:
    file.write(output)