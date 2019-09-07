# import the necessary dependencies for os.path.join()
import os
import csv

#set up an absolute path
csvpath = os.path.join('Resources', 'election_data.csv')
#read in a .csv file

#Your task is to create a Python script that analyzes the votes and calculates 
# each of the following:

    #The total number of votes cast
    #A complete list of candidates who received votes
    #The percentage of votes each candidate won
    #The total number of votes each candidate won
    #The winner of the election based on popular vote. 

#write a function that does:
    # Total number of votes cast
    # List of candidates
    # Percentage of votes each candidate won
    # Total number of votes each candidate won
    # Winner of election

# Define the function and have it accept the 'election_data' as its sole parameter
def election_info(csv):
    
    # For readability, it can help to assign your values to variables with descriptive names
    
    voter_id = ""
    county_id = ""
    cand_name = ""
    votes = 0
    #total_votes = 0
    votes_Khan = 0
    votes_Correy = 0
    votes_Li = 0
    votes_OTooley = 0
    percent_Khan = 0
    percent_Correy = 0
    percent_Li = 0
    percent_OTooley = 0
    candidate = ""
    win_candidate = ""

  
    for row in csv:
        votes += 1
        total_votes=votes - 1
        cand_name=row[2]
        

    #return cand_name
        if cand_name == "Khan":
            votes_Khan += 1
        elif cand_name == "Correy":
            votes_Correy += 1
        elif cand_name == "Li":
            votes_Li += 1
        elif cand_name == "O'Tooley":
            votes_OTooley += 1
        
        percent_Khan=votes_Khan/votes
        percent_Correy=votes_Correy/votes
        percent_Li=votes_Li/votes
        percent_OTooley=votes_OTooley/votes

    #return winning candidate
    if votes_Khan > votes_Correy and votes_Khan > votes_Li and votes_Khan > votes_OTooley:
        win_candidate = "Khan"
    elif votes_Correy > votes_Khan and votes_Correy > votes_Li and votes_Correy > votes_OTooley:
        win_candidate = "Correy"
    elif votes_Li > votes_Khan and votes_Li > votes_Correy and votes_Li > votes_OTooley:
        win_candidate = "Li"
    elif votes_OTooley > votes_Khan and votes_OTooley > votes_Correy and votes_OTooley > votes_Li:
        win_candidate = "OTooley"
        

#format votes_<candidate> to thousands
    total_votes = '{:,}'.format(votes)
    votes_Khan = '{:,}'.format(votes_Khan)
    votes_Correy = '{:,}'.format(votes_Correy)
    votes_Li = '{:,}'.format(votes_Li)
    votes_OTooley = '{:,}'.format(votes_OTooley)

#format percent_<candidate> to percent
    percent_Khan = '{0:.2%}'.format(percent_Khan)
    percent_Correy = '{0:.2%}'.format(percent_Correy)
    percent_Li = '{0:.2%}'.format(percent_Li)
    percent_OTooley = '{0:.2%}'.format(percent_OTooley)
    

    return [total_votes, votes_Khan, percent_Khan, votes_Correy, percent_Correy, votes_Li, percent_Li, votes_OTooley, percent_OTooley, win_candidate] 


# Read file using CSV module
with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    analysis = election_info(csvreader)
   


 #print Election Analysis
    print ("Election Results")
    print("----------------------------------------")
    print(f"Total Votes: {analysis [0]}")
    print("----------------------------------------")
    print(f"Kahn: {analysis [1]}  ({analysis[2]})")
    print(f"Correy: {analysis [3]}  ({analysis[4]})")
    print(f"Li: {analysis [5]}  ({analysis[6]})")
    print(f"O'Tooley: {analysis [7]}  ({analysis[8]})")
    print("----------------------------------------")
    print(f"Winner: {analysis[9]}")
    print("----------------------------------------")
            
    
    # Create the path for the filename
    data_output = os.path.join("Resources", "pypoll.txt")
        
    # Write data to a text file
    with open(data_output, "w") as file:    
        
        
        file.write("Election Results\n")
        file.write("----------------------------------------\n")
        file.write(f"Total Votes: {analysis [0]}\n")
        file.write("----------------------------------------\n")
        file.write(f"Kahn: {analysis [1]}  ({analysis[2]})\n")
        file.write(f"Correy: {analysis [3]}  ({analysis[4]})\n")
        file.write(f"Li: {analysis [5]}  ({analysis[6]})\n")
        file.write(f"O'Tooley: {analysis [7]}  ({analysis[8]})\n")
        file.write("----------------------------------------")
        file.write(f"Winner: {analysis[9]}")
        file.write("----------------------------------------")
        file.close()
   
   
   
    
    
            
        
       

    
