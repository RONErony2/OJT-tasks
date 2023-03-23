# 9. Given a string "abcde", Display the output as "a1b2c3d4e5"

# 1st approach
string = input("Enter the string : ")

res = ""
for i in range(len(string)):
    res += string[i]+str(i+1)

print(res)


# 2nd approach
string = input("Enter the string : ")

res = ""

for i, c in enumerate(string, start=1):
    res += c+str(i)

print(res)