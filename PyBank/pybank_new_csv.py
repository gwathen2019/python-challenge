# import the necessary dependencies for os.path.join()
import os
import csv

#set up an absolute path

#read in a .csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

#write a function that does:
    ## Number of months
    ## Net profit
    ## Greatest profit and Month
    ## Greatest loss and month
    ## Average change
    ## Print the information

def get_info(csv):
    months = 0
    total = 0
    max_revenue = 0
    min_revenue = 0
    avg_change = 0
    max_month = ""
    min_month = ""
    for row in csv:
        current_month = row[0]
        pnl = int(row[1])
        #total += pnl
        months += 1
        if pnl > max_revenue:
            max_revenue = pnl
            max_month = month
    return [months, total, max_month, max_revenue, min_month, min_revenue]


# Read file using CSV module
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    analysis = get_info(csvreader)
    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")




#with open (path) as file
    #csvreader = csv.reader(file, delimiter =",")
    #header = next csvreader
    #analysis = get_info(csvreader)

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)



print (analysis[0, 1])


    # Read each row of data after the header
    #for row in csvreader:
        #add Total
        #Total.append (row[1])
        #Total = [row[1]]
        #Tot_profit = [sum(len(Total))]
        #print(f"Total:  {Total}")