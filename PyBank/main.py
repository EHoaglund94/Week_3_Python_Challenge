import os
import csv

#Path to collect data form the Resources folder
bank_csv = os.path.join('Resources', 'budget_data.csv')

#Variables
month_list = []
revenue_list = []
total_revenue = 0
total_change = 0
change_max = [ '', 0]
change_min = [ '', 0]



with open (bank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvfile)
    



    #Read through rows in CSV file
    for row in csvreader:
        month_year = row[0]
        revenue = float(row[1])
        month_list.append(month_year)
        revenue_list.append(revenue)
        total_revenue += revenue

#loop through lists to find Financial Analysis outputs
total_months = len(month_list)

for i in range(1,total_months): 
    month_change = revenue_list[i] - revenue_list[i-1]
    total_change += month_change


average_change = total_change / (total_months-1 )
print (average_change)
print(total_months)
