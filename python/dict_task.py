# 23. create 2 dictionaries as follows:
# dict1 = {'name': 'Msys', 'Place': 'Pune'}
# dict2 = {'EmpID': 0001, 'Salary': 50000}
# Perform following operations:
# a. create single dictionary by merging dict1 & dict2
# b. update the salary to 10%
# c. update age to 35
# d. extract & print all the values & keys separetly in tuple.
# e. delete the element with key 'Age' & print the dictionary elements.

dict1 = {'name': 'Msys', 'Place': 'Pune'}
dict2 = {'EmpID': 2982, 'Salary': 50000}

# a. create single dictionary by merging dict1 & dict2
for key, val in dict2.items():
    dict1[key] = val

print(dict1)

# b. update the salary to 10%
sal = dict1['Salary']
sal = int(sal + (sal*(10/100)))

print(f"Salary before increment : {dict1['Salary']}")
dict1['Salary'] = sal
print(f"Slary after increment : {dict1['Salary']}")

# c. update age to 35
dict1['age'] = 35
print(dict1)

# d. extract & print all the values & keys separately in tuple.
print("Keys : ",tuple(dict1.keys()))
print("Values : ",tuple(dict1.values()))

# e. delete the element with key 'Age' & print the dictionary elements.
# del(dict1['age'])
print(dict1.pop('age'))
for key, value in dict1.items():
    print(key, " --> ", value)

