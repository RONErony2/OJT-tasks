# 6.Write a function to_percent which accepts a number representing a ratio and 
# returns a string representing the percentage representation of the number to one decimal place.
import re

def to_percent(ratio):
    if re.search(r"^[-+]?\d*\.\d*$",ratio):
        return f"{float(ratio)*100: .1f}"
    else:
        N,D = re.split(r":|/", ratio)
        return f"{(float(N)/float(D))*100: .1f}"

ratio = input("Enter the ratio : ")
print(f"{to_percent(ratio)} %")