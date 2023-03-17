# 10. In the given String -- ‘MsYs TecHNOlogiEs iS a gREat place To woRk’ find the count of
# lowercase and uppercase letters.

# 1st approach
string = input("Enter the string : ")

res = {'lower_count' : 0, 'upper_count' : 0}

for char in string:
    if char.isupper():
        res['upper_count'] += 1
    elif char.islower():
        res['lower_count'] += 1

print(res)

# 2nd approach
# lower_count = sum([1 for char in string if char.islower()])
# upper_count = sum([1 for char in string if char.isupper()])

# print("Number of lowercase letters:", lower_count)
# print("Number of uppercase letters:", upper_count)
