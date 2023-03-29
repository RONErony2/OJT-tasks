# 9. For the given sentence, return the average word length. 
# sentence = "I need to work very hard to learn more about algorithms in Python!" 
# Note: Remember to remove punctuation first.

import string

sentence = input("Enter the sentence : ")

sentence = sentence.translate(str.maketrans('','',string.punctuation))

words = sentence.split()

num_of_chars = sum(len(word) for word in words)
avg_len = num_of_chars/len(words)

print(round(avg_len, 1))