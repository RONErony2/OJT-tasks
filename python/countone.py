# 25. Given an Integer n, count the total number of times 1 is appearing in all 
# non-negative integers less than or equal to n. 
# Ex – n = 13, output should be 6 
# method – 1 is coming 6 times starting from number 0 till 13 in ‘1’, ‘10’, ‘11’, ‘12’, ‘13’. 
# Also note 1 is coming 2 times in 11. That is why 6 is the output

def count_num_of_one(n):
    num = 0
    res = 0
    while num <= n:
        str_num = str(num)
        if '1' in str_num:
            res += str_num.count('1')
        num+=1
    return res

n = int(input("Enter the number :"))
print(count_num_of_one(n))