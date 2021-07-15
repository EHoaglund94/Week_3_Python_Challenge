#Import modules
import os
import csv


#Path to collect data form the Resources folder
bank_csv = os.path.join('Resources', 'budget_data.csv')

#Set Variables
month_list = []
revenue_list = []
total_revenue = 0
total_change = 0
change_max = [ '', 0]
change_min = [ '', 0]


#Read CSV file
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

#Calculation to find total months
total_months = len(month_list)

#Loop through lists to find Financial Analysis outputs
for i in range(1,total_months): 
    month_change = revenue_list[i] - revenue_list[i-1]
    total_change += month_change
    if month_change > change_max[1] :
        change_max = [month_list[i], month_change]
    if month_change < change_min[1] :
        change_min = [month_list[i], month_change]

average_change = total_change / (total_months-1 )


#Put Summary Data into a list
summary_data = []
line1 = 'Financial Analysis'
line2 = '-' * 30
line3 = (f'Total Months: {total_months}')
line4 = (f'Total: $ {round(total_revenue)}')
line5 = (f'Average Change: ${round(average_change,2)}')
line6 = (f'Greatest Increase in Profits: {change_max[0]}  ({change_max[1]})')
line7 = (f'Greatest Decrease in Profits:  {change_min[0]}  ({change_min[1]})')
summary_data.extend([line1,line2,line3,line4,line5,line6,line7])

#Print results to terminal
for line in summary_data:
    print(line)



#Export results to text file
output_text = open('PyBank_outputs.txt', 'w')
with open('PyBank_outputs.txt', 'w') as txt_file:
    for line in summary_data:
        txt_file.write(line + '\n')


