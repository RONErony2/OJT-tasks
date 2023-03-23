# 7 In the given string, remove the special characters and add a space instead of that 
# "Msys&Technologies@Chennai*"

import re

def remove_special_characters(string):
    res = re.sub(r"\W", " ", string)
    return res

string = input("Enter the string : ")

print(remove_special_characters(string))