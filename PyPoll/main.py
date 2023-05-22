#import os to allow us create paths dinamically
import os
#import csv to allow us do manipulations with .csv files
import csv

#Path of resources to be read
election_data_csv = os.path.join('../PyPoll/Resources/election_data.csv')

#A variable for total votes
Tvotes=0
#Candidates list
Candi=[]
#This list for number of votes for each candidate
Candi_votes=[]
#Another list for votes percentage recieved per each candidate
Candi_percent=[]

#Open function to open resources file which is a .csv file 
with open(election_data_csv, encoding='UTF-8') as csvfile:
    #read it with seperation using "," 
    csvreader = csv.reader(csvfile, delimiter=",")
    #to jump to next row since 1st row is only words
    csv_header = next(csvfile)

    #loop through row to read n manipulate data
    for row in csvreader:
        #count number of total votes 
        Tvotes +=1
        #Check if we have added a new candidate or not
        #This is a way to get rid of iterated names
        #If we haven't then
        if row[2] not in Candi:
            Candi.append(row[2])
            index=Candi.index(row[2])
            Candi_votes.append(1)
        #If yes we the candidate is already there then
        else:
            index=Candi.index(row[2])
            Candi_votes[index] +=1

    #Now we loop through number of votes list to calculate the percentage for each candidate 
    for votes in Candi_votes:
        Percent= round((votes/Tvotes)*100,3)
        Candi_percent.append(Percent)

    #Finding the person with the highest percentage
    highest = max(Candi_percent)
    index= Candi_percent.index(highest)
    winner = Candi[index]

#Now printing to terminal
print("Election Results")
print("-------------------------")
print("Total Votes:  " +str(Tvotes))
print("-------------------------")
#We loop through each candidate with its index and print his/her name , his/her receieved votes percent and number of votes
for i in range(len(Candi)):
    print(f"{Candi[i]} :  " + str((Candi_percent[i])) + "%    (" + str((Candi_votes[i]))+ ")")
print("-------------------------")
print("Winner:  "+winner)
print("-------------------------")

#assigning a file and path to write results
results_txt=os.path.join('../PyPoll/analysis/PyPoll_Results.txt')
#we open a text file 
with open(results_txt, 'w') as txtfile:
    #let python start printing the data into the text file
     txtfile.write("Election Results" + '\n')
     txtfile.write("-------------------------" + '\n')
     txtfile.write("Total Votes:  " +str(Tvotes) + '\n')
     txtfile.write("-------------------------"+ '\n')
     #We loop through each candidate with its index and print his/her name , his/her receieved votes percent and number of votes
     for i in range(len(Candi)):
        txtfile.write(f"{Candi[i]} :  " + str((Candi_percent[i])) + "%    (" + str((Candi_votes[i])) + ")" + '\n')
     txtfile.write("-------------------------"+ '\n')
     txtfile.write("Winner:  "+winner + '\n')
     txtfile.write("-------------------------")
     #To close the text file
     txtfile.close()