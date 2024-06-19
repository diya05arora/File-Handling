# File: A storage space where you can save data on permanent basis
# how data can be persisted in Python? -> file Handling
# Types -> .csv, .xls or .xlsx (Excel file), .json (object file)

# .csv files (Comma separated file)
#  Two ways -> csv module and pandas

# csv module
import csv 
# Create a simple file and use it for writing
# a file can have in general 2 modes -> 'w' for writing and 'r' for reading

# WRITING
'''
with open("firstfile.csv", "w", newline='') as fileObj:
    writer = csv.writer(fileObj) # default delimiter = ","
    writer.writerow(["EmployeeId", "EmployeeName", "EmployeeSalary", "Department"])
    writer.writerow([101, "Ajay", 40000, "Marketing"])
    writer.writerow([102, "Aman", 70000, "Production"])
    writer.writerow([103, "Ankit", 30000, "Finance"])

data_list = [
    ["EmployeeId", "EmployeeName", "EmployeeSalary", "Department"],
    [101, "Ajay", 40000, "Marketing"],
    [103, "Ankit", 30000, "Finance"],
    [104, "Aditya", 90000, "Finance"],
]
with open("secondFile.csv", "w", newline="") as f:
    writer=csv.writer(f, delimiter="|") #delimiter should be single character
    writer.writerows(data_list)

data_list = [
    ["EmployeeId", "EmployeeName", "EmployeeSalary", "Department"],
    [101, "Ajay", 40000, "Marketing"],
    [103, "Ankit", 30000, "Finance"],
    [104, "Aditya", 90000, "Finance"],
]
with open("thirdFile.csv", "w", newline="") as f:
    writer=csv.writer(f, delimiter="|", quotechar='*', quoting=csv.QUOTE_NONNUMERIC) #delimiter should be single character
    writer.writerows(data_list)

data_list = [
    ["EmployeeId", "EmployeeName", "EmployeeSalary", "Department"],
    [101, "Ajay", 40000, "Marketing"],
    [103, "Ankit", 30000, "Finance"],
    [104, "Aditya", 90000, "Finance"],
]
with open("fourthFile.csv", "w", newline="") as f:
    writer=csv.writer(f, delimiter="|", quotechar='"', quoting=csv.QUOTE_ALL) #delimiter should be single character
    writer.writerows(data_list)
'''

# READING
'''
with open("secondFile.csv", "r") as f: # deafault mode is "r" only
    reader = csv.reader(f, delimiter="|", skipinitialspace=True)
    # skipinitialspace removes the initial space if present before any element
    for row in reader:
        print(row)

with open("fourthFile.csv", "r") as f: # deafault mode is "r" only
    reader = csv.reader(f, delimiter='|', quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=False)
    for row in reader:
        print(row)

with open("fourthFile.csv", "r") as f: # deafault mode is "r" only
    reader = csv.reader(f, delimiter='|', quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    for row in reader:
        print(row)
'''
with open("firstfile.csv", "w+", newline='') as fileObj:
    writer = csv.writer(fileObj) # default delimiter = ","
    writer.writerow(["EmployeeId", "EmployeeName", "EmployeeSalary", "Department"])
    writer.writerow([104, "Ajay", 40000, "Marketing"])
    writer.writerow([105, "Aman", 70000, "Production"])
    writer.writerow([106, "Ankit", 30000, "Finance"])