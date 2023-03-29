# 11. From the given list, check if the element is an integer then return square of that element 
# and if element is a string then return the same string 2 times. Output should be in list format. 
# a = [8,9,10,"f",5,8,"d"] 
# Output should be : [64, 81, 100, 'ff', 25, 64, 'dd']

def check_int(val):
    if type(val) == int:
        return True
    return False

def check_str(val):
    if type(val) == str:
        return True
    return False

list1 = [8,9,10,"f",5,8,"d",10.5]

for i in range(len(list1)):
    val = list1[i]
    if check_int(val):
        list1[i] = val**2
    elif check_str(val):
        list1[i] = val*2

print(list1)
