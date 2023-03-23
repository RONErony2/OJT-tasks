# 6. Define the logic for generating the email id based on username and department 
# Get the username and department as a input and create a email id from it input: 
# output: 
# username: msys 
# department: automation 
# msys.automation@gmail.com 
# Note: Generated email id should contain @ and should end with.com 

def generate_mail_id(usr_name, dept):
    return f"{user_name}.{dept}@gmail.com"

user_name = input("Enter the user name : ")
department = input("Enter the department name : ")

print(generate_mail_id(user_name, department))