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