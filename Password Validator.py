# Alex Coffman 22/JUL/23
# CMIS 102/6980 Week 6 Assignment
# This program verifies that a given password meets the following requirements:
    # has a min and max password length
    # contains no spaces
    # has atleast one alpha character and one digit
# Welcome message for the user
print("\nWelcome to the password validator\n")
print("This program will check to see if your password meets the predetermined requirements!")

# This function sets the desired length by returning the length of the password and checking if it is within the determined min/max length
def passwordLength(userPassword, minLength, maxLength):
    length = len(userPassword)
    return minLength <= length <= maxLength 

# This function checks to see if the password contains a digit and a alpha character
def passwordCharacters(userPassword):
    # Set both passDigit and passAlpha to false as default
    passDigit = False
    passAlpha = False
    # Examines characters in the input using if/elif statements to check if digit and alpha are true using the 'for' loop
    for char in userPassword:
        if char.isdigit():
            passDigit = True
        elif char.isalpha():
            passAlpha = True
    return passDigit and passAlpha 

# This function checks to see if there are spaces present in the password
def passwordSpaces(userPassword):
    # Checks 'if' a space is 'in' user input
    if ' ' in userPassword:
        return False 
    return True 
    
# Main program that calls the above functions for evaluation
def main():
    # Sets the minimum and maximum length for the allowed password
    minLength = 8
    maxLength = 20   
    # Prompts the user to input their password to be verified
    userPassword = input("\nPlease enter your password for verification: ")  
    # Checks the password conditions for false outputs
    if not passwordLength(userPassword, minLength, maxLength):
        print("The password doesn't meet the min/max length requirement")
        return
    if not passwordCharacters(userPassword):
        print("The password must contain at least one number: 0-9 and one alpha character: a-z")
        return 
    if not passwordSpaces(userPassword):
        print("Your password contains an invalid space")
        return    
    # If all parameters are met and the password is valid
    print("Valid password")

main()