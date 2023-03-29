# 7. Reverse the below string without changing the position of special characters . 
# s = "adfw$vf&yvy*ugv%uy"

s = input("Enter the string : ")

special_char = "~`!@#$%^&*()_-+={[]}|\\?/><:;\"'.,"

res = list(s)

i = 0
j = len(s)-1

while i < j:
    while s[i] in special_char:
        i += 1

    while s[j] in special_char:
        j -= 1

    if i < j:
        res[i],res[j] = res[j],res[i]
        i += 1
        j -= 1

res = "".join(res)

print(res)


