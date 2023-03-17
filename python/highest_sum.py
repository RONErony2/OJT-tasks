# Find the highest sum of the string by removing the duplicates for each iteration
# input=’1211’
# output:3

from collections import defaultdict

# 1st approach
string = input("Enter the string : ")

unique_elements = set([int(i) for i in string])

print(f"output : {sum(unique_elements)}")


#2nd approach
unique_elements = defaultdict(int)

for i in string:
    unique_elements[int(i)] += 1

print(f"output : {sum(dict(unique_elements).keys())}")








