# 23.Write a logic for calculating the time taken for executing the python function

import time

start = time.time()

string = input("Enter the string : ")

res = {'lower_count' : 0, 'upper_count' : 0}

for char in string:
    if char.isupper():
        res['upper_count'] += 1
    elif char.islower():
        res['lower_count'] += 1

print(res)

end = time.time()


print(f"Toatal time : {end - start : .2f}")