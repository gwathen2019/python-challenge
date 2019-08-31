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
    change_in_rev_sum = 0
    prev_pnl = 0
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

        change_in_rev = pnl_int - prev_pnl
        change_in_rev_sum =+ change_in_rev
        if change_in_rev > max_revenue:
            max_revenue = change_in_rev
            max_month = current_month
        
        elif change_in_rev < min_revenue:
            min_revenue = change_in_rev
            min_month = current_month

        prev_pnl = pnl_int
        
    avg_change = change_in_rev_sum/(months-1)

    #format total, avg_change, max_revenue, min_revenue to USD format
    total = '${:,.2f}'.format(total)
    avg_change = '${:,.2f}'.format(avg_change)
    max_revenue = '${:,.2f}'.format(max_revenue)
    min_revenue = '${:,.2f}'.format(min_revenue)

    return [months, total, avg_change, max_month, max_revenue, min_month, min_revenue]
    
# Read file using CSV module
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    analysis = get_info(csvreader)

    # Create the path for the filename
    data_output = os.path.join("Resources", "pybank.txt")
        
    # Write data to a text file
    with open(data_output, "w") as file:    
        
        #file = open(“pybank1.txt”, “w”)
        file.write ("Financial Analysis\n")
        file.write ("----------------------------------------\n")
        file.write (f"Total Months: {analysis [0]}\n")
        file.write (f"Total: {analysis[1]}\n")
        file.write (f"Average Change: {analysis[2]}\n")
        file.write (f"Greatest Increase in Profits: {analysis [3]}, {analysis [4]}\n")
        file.write (f"Greatest Decrease in Profits:  {analysis [5]}, {analysis [6]}\n")
        file.close()
   
   
    #print Financial Analysis
    #with open('Resources', 'pybank1.txt', 'w') as file:
        #for line in file:
            #print ("Financial Analysis")
            #print("----------------------------------------")
            #print(f"Total Months: {analysis [0]}")
            
            #print (f"Total: {analysis[1]}")
            #print (f"Average Change: {analysis[2]}")
            #print (f"Greatest Increase in Profits: {analysis [3]}, {analysis [4]}")
            #print (f"Greatest Decrease in Profits:  {analysis [5]}, {analysis [6]}")

    #write output to text file

    
