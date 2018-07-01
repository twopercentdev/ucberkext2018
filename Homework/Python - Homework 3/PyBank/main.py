import os
import csv
import math

dirname=os.path.dirname
budgetDataPath = os.path.join(dirname(__file__), "Resources", "budget_data.csv")

budget = dict()

with open(budgetDataPath, newline="") as csvfile:
    reader = csv.DictReader(csvfile)
   
    for row in reader:
        key = row['Date']
        budget[key] = int(row['Revenue'])

budgetMonths = len(budget)
budgetSum = sum(budget.values())
budgetMean = budgetSum/budgetMonths

budgetMaxKey = max(budget, key=budget.get)
budgetMax = max(budget.values())

budgetMinKey = min(budget, key=budget.get)
budgetMin = min(budget.values())

print ('Financial Analysis\n----------------------------\nTotal Months: '+ str(budgetMonths) + '\nTotal: $' + str(budgetSum) + '\nAverage  Change: $' + str(round(budgetMean,2)) + '\nGreatest Increase in Profits: ' + budgetMaxKey + ' $' + str(budgetMax) + '\nGreatest Decrease in Profits: ' + budgetMinKey + ' $' + str(budgetMin))

with open('Financial Analysis.csv','w') as csvfile:
    print ('Financial Analysis\n----------------------------\nTotal Months: '+ str(budgetMonths) + '\nTotal: $' + str(budgetSum) + '\nAverage  Change: $' + str(round(budgetMean,2)) + '\nGreatest Increase in Profits: ' + budgetMaxKey + ' $' + str(budgetMax) + '\nGreatest Decrease in Profits: ' + budgetMinKey + ' $' + str(budgetMin), 'Financial Analysis.csv', file=f)
