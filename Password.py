# First Project: Password Strength Checker and Logger

# Prompt the user to enter their password
n = input("Enter Password : ") 

# Check if the password length is less than 6 characters
if len(n) < 6: 
    print("Weak password") 
    
    # Open the file in write mode and log the result as "Weak"
    file = open("password.txt", "w")
    file.write("Weak")
    file.close()

# Check if the password length is 6 or more characters
if len(n) >= 6:
    print("Strong password")
    
    # Open the file in write mode and log the result as "Strong"
    file = open("password.txt", "w")
    file.write("Strong")
    file.close() # Closing the file to ensure the data is saved properly
    
    # Open the file in read mode to fetch the saved data
    file = open("password.txt", "r")
    data = file.read()
    
    # Print the data retrieved from the file onto the screen
    print(data)
    file.close()
