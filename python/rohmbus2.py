# 22. Print the following rhombus pattern . eg. If input is 4, it should print the following output .
#    1
#   2 2
#  3 3 3
# 4 4 4 4
#  3 3 3
#   2 2
#    1

# 1st approach
def rohmbus_triangle(num):
    temp = 0
    for i in range(1, num*2):
        if i <= num:
            x, y = num-(i-1), num+(i-1)
            temp += 1
        else:
            x = i-num+1
            y = (num*2)-x
            temp -= 1
        char = True
        for j in range(1,num*2):
            if j >= x and j <= y and char:
                print(temp, end = "")
                char = False
            else:
                print(" ", end="")
                char = True
        print()

num = int(input("Enter the number : "))

rohmbus_triangle(num)

# 2nd approach

def print_rhombus(n):
    # upper half of rhombus
    for i in range(1, n+1):
        # print spaces before numbers
        print(" "*(n-i), end="")
        # print numbers
        print((str(i)+" ")*i)
    # lower half of rhombus
    for i in range(n-1, 0, -1):
        # print spaces before numbers
        print(" "*(n-i), end="")
        # print numbers
        print((str(i)+" ")*i)

# example usage with n=4
print_rhombus(5)
