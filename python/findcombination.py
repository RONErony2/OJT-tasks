# 24. You have given a string str1 = "abcbaefabcabchijkl"
# your task is to find the combination of given word without repetition, present in the string , given
# word 'abc'
# o/p = 7
# explaination :
# abc, cba, cba, bca, acb, cab, bac

import itertools

def find_combination_of_word(string, word):
    
    combinations = set([''.join(p) for p in itertools.permutations(word)])

    count = 0

    for combination in combinations:
        if combination in string:
            count += 1
    return count

string = input("Enter the string : ")
word = input("Enter the word : ")

print(find_combination_of_word(string, word))