# 20. Write a python program for sort the given below list based last character of each word
# names_list = ['Prabhu', Rahul', 'Arunesh, 'Sonali', 'Rakshit']

names_list = [name for name in input("Enter the space separated names : ").split()]

length = len(names_list)

for i in range(length):
    for j in range(i+1,length):
        if names_list[i][-1] > names_list[j][-1]:
            names_list[i], names_list[j] = names_list[j], names_list[i]

print(names_list)