import csv
import os

csv_path = os.path.join("Resources","budget_data.csv")

change = []
with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    months = 0
    mon = []
    net = 0
    csv_header = next(csvfile)
    for row in csvreader:
        months = months + 1
        net = net + int(row[1])
        change.append(row[1])
        mon.append(row[0])
        
diff=[]
def avg(seq):
    total = 0
    for i in range(len(seq)):
        diff.append(int(seq[i])-int(seq[i-1]))
    length = len(diff)-1
    for row in diff:
        total += row
    return (total-diff[0])/length

ok = str(round(avg(change),2))
big = max(diff)
small = min(diff)

new = zip(mon,diff)
greatest = [num for num in new if num[1] == max(diff)]

newer = zip(mon,diff)
smallest = [nub for nub in newer if nub[1] == min(diff)]

output_file = os.path.join("test.csv")
with open(output_file, "w", newline="") as test:
    writer = csv.writer(test)

    writer.writerows(new)

with open("PyBank.txt","w") as outfile:
    outfile.write("Financial Analysis \n")
    outfile.write("---------------------- \n")
    outfile.write(f"Total Months: {months}\n")
    outfile.write(f"Total: ${net} \n")
    outfile.write(f"Average Change: ${ok} \n")
    outfile.write(f"Greatest Increase in Profits: {greatest[0][0]}: ${big} \n")
    outfile.write(f"Greatest Decrease in Profits: {smallest[0][0]}: ${small} \n")
    
print("Financial Analysis \n")
print("---------------------- \n")
print(f"Total Months: {months}\n")
print(f"Total: ${net} \n")
print(f"Average Change: ${ok} \n")
print(f"Greatest Increase in Profits: {greatest[0][0]}: ${big} \n")
print(f"Greatest Decrease in Profits: {smallest[0][0]}: ${small} \n")