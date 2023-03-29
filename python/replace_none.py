# 14. In the given list, check if the element is None, replace it with the recent value .
# l = [1,None,None,3,None,4] Output should be : [1,1,1,3,3,4]

list1 = [1,None,None,3,None,4,None,None,5,None]

recent_val = None

for i in range(len(list1)):
    if not list1[i]:
        list1[i] = recent_val
    else:
        recent_val = list1[i]

print(list1)

