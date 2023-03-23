# 6.Write a function to_percent which accepts a number representing a ratio and 
# returns a string representing the percentage representation of the number to one decimal place.
import re

class ImproperValue(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
    
def to_percent(ratio):
    try:
        if re.search(r"^[-+]?\d*\.\d*$",ratio):
            return f"{float(ratio)*100: .1f}"
        elif re.search(r"^\d+[:/][123456789]+$",ratio):
            N,D = re.split(r":|/", ratio)
            return f"{(float(N)/float(D))*100: .1f}"
        else:
            raise ImproperValue("Enter the proper ratio value.")
    except ImproperValue as err_msg:
        print(f"ImproperValue : {err_msg}")

ratio = input("Enter the ratio : ")
res = to_percent(ratio)
if res != None:
    print(f"{res} %")