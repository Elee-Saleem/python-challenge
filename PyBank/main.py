#import os to allow us create paths dinamically
import os
#import csv to allow us do manipulations with .csv files
import csv

#Path of resources to be read
Budget_data_csv = os.path.join('../PyBank/Resources/budget_data.csv')

#We count total months
Tmonths =0
#We create veriable for total money
netTotal =0
#A list for Month over Month change
MoMchange = []
#Variable for Profit-Loss change for a single month
PLchange =0
#Variable for previous month Profit-Loss 
previous =0
#A date list later will be used for greatest changes
date =[]

#Open function to open resources file which is a .csv file 
with open(Budget_data_csv, encoding='UTF-8') as csvfile:
    #read it with seperation using "," 
    csvreader = csv.reader(csvfile, delimiter=",")
    #to jump to next row since 1st row is only words
    csv_header = next(csvreader)
    #another jump so now we start reading from here
    row0 =next(csvreader)

    #we start count months now
    Tmonths += 1
    #calculating total money
    netTotal += int(row0[1])
    #now this is previous month before it changes 
    previous = int(row0[1])
    #loop through row to read n manipulate data
    for row in csvreader:
        #finding the month over month profit-loss change
        PLchange=int(row[1])-previous
        MoMchange.append(PLchange)
        #recording date
        date.append(row[0])
        #counting another month
        Tmonths += 1
        #adding another monthly money
        netTotal += int(row[1])
        #now previous month money has changed 
        previous= int(row[1])
    #calculating the average change in monthly profit loss len function is to find the length of content
    Average_PLchange= round(sum(MoMchange)/len(MoMchange),2)
    #finding the max increase in profit-loss month over month change with its date
    Max_increase =max(MoMchange)
    Max_increase_index = MoMchange.index(Max_increase)
    Max_increase_date= date[Max_increase_index]
    #finding the lowest decrease in profit-loss month over month change with its date
    Max_decrease=min(MoMchange)
    Max_decrease_index=MoMchange.index(Max_decrease)
    Max_decrease_date=date[Max_decrease_index]
#now printing
print("Financial Analysis")
print("----------------------------")

print("Total Months:  " + str(Tmonths))
#net total of all monthly profit-loss earnings
print("Total:  " + str(netTotal))
#amount of avergae change of monthly earning
print("Average Change:  $" + str(Average_PLchange))
#greatest increase and decrease in monthy profit-loss changes
print("Greatest Increase in Profits:  " + str(Max_increase_date) + " ($" + str(Max_increase) + ")")
print("Greatest Decrease in Profits:  " + str(Max_decrease_date) + " ($" + str(Max_decrease) +")")

#assigning a file and path to write results
results_txt=os.path.join('../PyBank/analysis/PyBank_Results.txt')
#we open a text file 
with open(results_txt, 'w') as txtfile:
    #let python start printing the data into the text file
    txtfile.write("Financial Analysis"+ '\n')
    txtfile.write("----------------------------"+ '\n')

    txtfile.write("Total Months:  " + str(Tmonths)+ '\n')

    txtfile.write("Total:  " + str(netTotal)+ '\n')
    
    txtfile.write("Average Change:  $" + str(Average_PLchange)+ '\n')
    
    txtfile.write("Greatest Increase in Profits:  " + str(Max_increase_date) + " ($" + str(Max_increase) + ")" + '\n')
    txtfile.write("Greatest Decrease in Profits:  " + str(Max_decrease_date) + " ($" + str(Max_decrease) + ")")
    #To close the text file
    txtfile.close() 