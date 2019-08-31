# import the necessary dependencies for os.path.join()
import os
import csv

#set up an absolute path
csvpath = os.path.join('Resources', 'budget_data2.csv')
#read in a .csv file
  

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
    change_in_rev = 0
    total_change = 0
    avg_change = 0
    max_month = ""
    min_month = ""
    #r.next()
    for row in csv:
        current_month = row[0]
        pnl = row[1]
        pnl_int = int(pnl)
        total += pnl_int
        months += 1

        if pnl_int > max_revenue:
            max_revenue = pnl_int
            max_month = current_month
        
        elif pnl_int < min_revenue:
            min_revenue = pnl_int
            min_month = current_month
        
        
        #change_in_rev = pnl - 
        #avg_change=total_change/months
    
    return [months, total, avg_change, max_month, max_revenue, min_month, min_revenue]
    
# Read file using CSV module
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    analysis = get_info(csvreader)
    #print(csvreader)
    print(analysis)

    #print Financial Analysis
    print ("Financial Analysis")
    print("----------------------------------------")
    print(f"Total Months: {analysis [0]}")

    print (f"Total: {analysis[1]}")
    print (f"Average Change: {analysis[2]}")
    print (f"Greatest Increase in Profits: {analysis [3]}, {analysis [4]}")
    print (f"Greatest Decrease in Profits:  {analysis [5]}, {analysis [6]}")

    print

#with open (path) as file
    #csvreader = csv.reader(file, delimiter =",")
    #header = next csvreader
    #analysis = get_info(csvreader)



#print (analysis[0, 1])


    # Read each row of data after the header
    #for row in csvreader:
        #add Total
        #Total.append (row[1])
        #Total = [row[1]]
        #Tot_profit = [sum(len(Total))]
        #print(f"Total:  {Total}")