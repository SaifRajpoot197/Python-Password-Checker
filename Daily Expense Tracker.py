# Taking three expenses as input from the user
n1 = int(input("Enter (1st) Expense: "))
n2 = int(input("Enter (2nd) Expense: "))
n3 = int(input("Enter (3rd) Expense: "))

# Calculating the total of all three expenses
total = n1 + n2 + n3

# Displaying the total expense
print("Total Expense:", total)

# Opening the file in write mode to save expenses
file = open("Expense.txt", "w")

# Writing all three expenses into the file
file.write("Expense 1: " + str(n1) + "\n")
file.write("Expense 2: " + str(n2) + "\n")
file.write("Expense 3: " + str(n3) + "\n")

# Writing the total expense into the file
file.write("Total Expense: " + str(total) + "\n")

# Closing the file after writing
file.close()

# Opening the file in read mode
file = open("Expense.txt", "r")

# Reading and displaying the saved data
data = file.read()
print("\nSaved Expenses:")
print(data)

# Closing the file after reading
file.close()