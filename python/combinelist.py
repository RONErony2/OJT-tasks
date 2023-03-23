# 10. Write a function combine_lists should take two lists and return a new list 
# containing all elements from both lists.

def combine_lists(list1, list2):
    #  1st approach
    list1[len(list1):] = list2
    return list1

    # 2nd approach
    # list = list1 + list2
    # return list

    # 3rd approach
    # list1.extend(list2)
    # return list1

list1 = [int(i) for i in input("Enter the list elements : ").split()]
list2 = [int(i) for i in input("Enter the list elements : ").split()]

print(combine_lists(list1, list2))
