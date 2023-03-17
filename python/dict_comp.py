# 7. Write a program using dictionary comprehension which will contain the key value pair of i:i**2.
# Value of ‘i’ will start from 1 and will go upto 10.

dict_ = {i : i**2 for i in range(1, 10)}
print(dict_)