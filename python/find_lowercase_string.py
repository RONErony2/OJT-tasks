# 6. Write a program to extract the words starting with lowercase letter present in the list. 
# [‘Nissan’, ‘maruti’, ‘hyundai’, ‘Volkswagen’, ‘audi’]

# 1st approach
def extract_string_startswith_lowercase(list_):
    a = ord('a')
    z = ord('z')
    res = []
    for string in list_:
        val = ord(string[0])
        if val >= a and val <= z:
            res.append(string)
    return res

list_ = [s for s in input().split()]
print(extract_string_startswith_lowercase(list_))

#2nd approach
# lowercase_words = [word for word in list_ if word[0].islower()]
# print(lowercase_words)