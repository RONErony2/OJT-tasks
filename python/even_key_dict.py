# 3. Create a dictionary where the key is an even number from the given list and the value 
#     will be the occurrence of that element in the list. input= [1,2,3,2,4,2,4,7,8,4,5,8,6,9,2] 
from collections import defaultdict

list1 = [int(i) for i in input().split()]

# 1st approach : Using dictionary comprehension.
unique_ele = set(list1)

even_key_dict = {i: list1.count(i) for i in unique_ele if i%2 == 0}

print(f"Output : {even_key_dict}")

# 2nd approach : Using loops.

even_key_dict = {}
length = len(list1) - 1

for i in list1:
    if i%2 == 0:
        if i in even_key_dict:
            even_key_dict[i] += 1
        else:
            even_key_dict[i] = 1

print(f"Output : {even_key_dict}")

# 3rd approach : Using defaultdict

even_key_dict = defaultdict(int)
for i in list1:
    if i % 2 == 0:
        even_key_dict[i] += 1

print(f"Output: {dict(even_key_dict)}")





        


