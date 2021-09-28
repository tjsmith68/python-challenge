
import os 

month_count = 0
total_profits = 0
total_delta = 0
current_delta = 0 
previous_profit = 0
current_profit = 0
current_month = " "
greatest_increase = 0
greatest_increase_month = " "
greatest_decrease = 0
greatest_decrease_month = " "
average_increase = 0

file = os.path.join('Resources','budget_data.csv')

filedata = open(file,"r")

stillreading = True

# Dummy read to skip headings line

line = filedata.readline()

# Loop to read remaining data

first_row = True

while stillreading:
    line = filedata.readline()
    item = line.split(",")
    #If no new row, set loop exit condition
    if item[0] == "":
        stillreading = False
    else:
        #Only process if you read a new line
        current_month = item[0]
        current_profit = int(item[1])
        total_profits = total_profits + current_profit
        if first_row:
            first_row = False
        else:
            #Only calculate and accumulate deltas if past the first row
            current_delta = current_profit - previous_profit
            total_delta = total_delta + current_delta
        previous_profit = current_profit
        month_count = month_count + 1
        if current_delta > greatest_increase:
            greatest_increase = current_delta
            greatest_increase_month = current_month
        if current_delta < greatest_decrease:
            greatest_decrease = current_delta
            greatest_decrease_month = current_month   

filedata.close()

# Note, there are 1 fewer 'deltas' than months accumulated
average_increase = round(total_delta/(month_count-1),2)

# Output the Analysis to the terminal
print("Financial Analysis")
print("--------------------------------------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${total_profits}")
print(f"Average Change: ${average_increase}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")


outfile = os.path.join('Resources','Analysis.txt')

fileout = open(outfile,"w")

# Output the Analysis to a file
fileout.write("Financial Analysis\n")
fileout.write("--------------------------------------------------------\n")
fileout.write(f"Total Months: {month_count}\n")
fileout.write(f"Total: ${total_profits}\n")
fileout.write(f"Average Change: ${average_increase}\n")
fileout.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
fileout.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")

fileout.close()