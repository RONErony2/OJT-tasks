# 7. Write a function that accepts two strings and returns True if the two strings are anagrams 
# of each other.

# 1at approach
def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    set_char = set(str1)
    for char in set_char:
        if str1.count(char) != str2.count(char):
            return False
    return True

str1 = input("Enter the string1 : ")
str2 = input("Enter the string2 : ")

res = is_anagram(str1, str2)

if res:
    print("Given strings are anagrams to each other")
else:
    print("Given strings are not anagrams to each other")


# 2nd approach
from collections import Counter

def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    dict_ = dict(Counter(str1))

    for c in str2:
        dict_[c]-=1
    
    for v in dict_.values():
        if v != 0:
            return False
    return True

str1 = input("Enter the string1 : ")
str2 = input("Enter the string2 : ")

res = is_anagram(str1, str2)

if res:
    print("Given strings are anagrams to each other")
else:
    print("Given strings are not anagrams to each other")