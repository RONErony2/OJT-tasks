# 17. Write a program to find the count of alphabet alone in the given alphanumeric string for
# Ex1: input=’abb24ccc8ddbbca1’ output=’a1b224c3d2b2c1a11’
# Ex2: input = ‘abc23’ output=’a1b1c123

string = input("Enter the string : ")

res = ""

length = len(string)

i = 0
while i < length:
    char = string[i]
    if char.isalpha():
        count = 1
        j = i+1
        while j < length and char == string[j]:
            count += 1
            j += 1
        res = res + char+str(count)
        i = j
    else:
        res += char
        i += 1
print(res)