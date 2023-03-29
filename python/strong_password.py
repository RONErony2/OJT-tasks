# 25. Write a function that employs regular expressions to ensure the password given to the 
# function is strong. A strong password is defined as follows: 
# -at least eight characters long 
# -contains one uppercase character 
# -contains one lowercase character 
# -has at least one digit 
# -has at least one special character

import re

def is_strong_password(password):
    if len(password) < 8:
        return False
    
    if not re.search(r'[A-Z]', password):
        return False
    
    if not re.search(r'[a-z]', password):
        return False
    
    if not re.search(r'\d', password):
        return False
    
    if not re.search(r'[~!@#$%^&*()_+{}":;\']', password):
        return False
    
    return True

password = input("Enter the password : ")

res = is_strong_password('password1')

if res:
    print("Given password is strong.")
else:
    print("Given password is not strong.")


