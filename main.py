# Importing the CSV module
import csv

# Opening or creating the file
with open("Data.csv", 'w', newline="") as file:
    myFile = csv.writer(file)

# Writing the column headers
    myFile.writerow(["First Name","Last Name","Date of Birth","Months","Income","Expenses"])

# Getting the number of rows to add
    no_of_months = int(input("Enter the number of months for the customers income and expenses: \n"))

# Using for loop to write user input to the file
    for i in range(no_of_months):
        fname = input("Enter the name of the customer: \n")
        lname = input("Enter the surname of the customer: \n")
        birth = input("Enter the date of birth of the customer in the form of DD/MM/YYYY: \n")
        month = input("Enter the month: \n")
        income = int(input("Enter the income amount: \n"))
        expenses = int(input("Enter the expenses amount: \n"))
        myFile.writerow([fname, lname, birth, month, income, expenses])
