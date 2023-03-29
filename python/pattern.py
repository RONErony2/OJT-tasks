# 23. Print the following pattern :
#      *
#     *-*
#    *---*
#   *-----*
#  *-------*
# *---------*

num = int(input("Enter the number : "))

r = 1
for i in range(1,num+1):
    if i != 1:
        print(" "*(num-i)+"*"+"-"*r+"*")
        r += 2
    else:
        print(" "*(num-i)+"*")

