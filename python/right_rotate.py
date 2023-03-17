# 1. Write a python program to right rotate a List by n
#      Enter position to rotate list item: 3 
#      Sample input: [10, 20, 30, 40, 50, 60, 70] 
#      Expected output: [50, 60, 70, 10, 20, 30, 40] .


list1 = [int(i) for i in input().split()]

position = int(input("Enter position to rotate list item: "))

length = len(list1)

position = position%length

# 1st approach : Using list built-in methods (pop, insert).

for i in range(position):
    pop_element = list1.pop()
    list1.insert(0, pop_element)

print(f"Output : {list1}")


# 2nd approach : Using slicing and concatenate operation.

rotate_list = list1[-(position):] + list1[:-(position)] 

print(f"Output : {rotate_list}")


# 3rd approach : Using loop concept.

length = len(list1)

for i in range(position):
    temp = list1[-1]
    for j in range(length - 1, 0, -1):
        list1[j] = list1[j - 1]
    list1[0] = temp

print(f"Output : {list1}")



