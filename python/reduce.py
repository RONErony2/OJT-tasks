# 10. Generate a dictionary from the two given lists using dict function (without using for loops) and 
# calculate the sum of all the values in the dictionary using reduce and anonymous concepts 
# L1 = ["a","b"] L2 = [1,2] 
# Expected Output: 
# data = {"a": 1, "b":2} 
# sum = 3

import functools as f

L1 = ['a', 'b', 'c', 'd']
L2 = [1, 2, 30, 4]

# print(zip(L1, L2))

dict_ = dict(zip(L1, L2))

print("data = ",dict_)

res = f.reduce(lambda a,b: a+b, dict_.values())

print("sum = ", res)