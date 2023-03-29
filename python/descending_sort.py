# 10. Sort the list of integers in descending order without using inbuilt functions . 
# lst = [56,2,13,1,78,4,6]

list_1 = [int(i) for i in input("Enter the space separated list value : ").split()]

length = len(list_1)

print("Before sort : ", list_1)

for i in range(length):
    for j in range(i,length):
        if list_1[i] < list_1[j]:
            list_1[i],list_1[j] = list_1[j], list_1[i] 

print("After sort : ",list_1)