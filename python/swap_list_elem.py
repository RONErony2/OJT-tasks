# 4. Write a function swap_element that contains two args which will be the position of 
#     elements present in the list. The function must swap the elements present in those 
#     positions. 
#     Input: [1,2,3,4,5,6,7,8] function: swap_element(arg1, arg2)


list1 = [int(i) for i in input().split()]

pos1 = int(input("Enter the position 1 : "))

pos2 = int(input("Enter the position 2 : "))

def swap_element(list1, pos):
    pos1, pos2 = pos
    try:
        if pos1 != pos2:
            list1[pos1], list1[pos2] = list1[pos2], list1[pos1]
            return list1
    except IndexError:
        print("Error : Enter the position within the range!..")

print(f"Before swap : {list1}")

list1 = swap_element(list1, (pos1, pos2))

print(f"After swap : {list1}")



