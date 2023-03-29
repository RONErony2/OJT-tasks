# 18. Print the below rohmbus pattern according to the given number
# for eg: given number is 4 then
# o/p will be
#    1
#   212
#  32123
# 4321234
#  32123
#   212
#    1

# 1st approach

def rohmbus_pattern(num):
    temp = 0
    for i in range(1,num*2):
        if i <= num:
            x,y = num-(i-1),num+(i-1)
            temp += 1
        else:
            x = i-num+1
            y = (num*2)-x
            temp -= 1
        temp1 = temp
        for j in range(1,num*2):
            if j>=x and j<=y:
                print(temp1,end=" ")
                if j < num:
                    temp1-=1
                else:
                    temp1+=1
            else:
                print(" ",end=" ")
        print()


num = int(input("Enter the number : "))
rohmbus_pattern(num)

# 2nd approach


def print_rhombus(n):
    # upper half of rhombus
    for i in range(1, n+1):
        # print spaces before numbers
        print(" "*(n-i), end="")
        # print numbers in decreasing order
        for j in range(i, 0, -1):
            print(j, end="")
        # print numbers in increasing order
        for j in range(2, i+1):
            print(j, end="")
        print()
    # lower half of rhombus
    for i in range(n-1, 0, -1):
        # print spaces before numbers
        print(" "*(n-i), end="")
        # print numbers in decreasing order
        for j in range(i, 0, -1):
            print(j, end="")
        # print numbers in increasing order
        for j in range(2, i+1):
            print(j, end="")
        print()

# example usage with n=4
print_rhombus(5)