# 13. Write a python program to take 2 inputs(numbers) from user. 
# Divide the greater number by the smaller number. 
# Validate the user inputs, it should be integer type only . 
# If the input is not integer, raise exception and catch it. 
# Also, if divisor is 0, catch the exception raised.

def check_numerator_dinominator(func):
    def wrapper(num1,num2):
        if num1<num2:
            num1, num2 = num2, num1
        return func(num1, num2)
    return wrapper

@check_numerator_dinominator
def division(num1, num2):
    try:
        if num2 == 0:
            raise ZeroDivisionError
    except ZeroDivisionError:
        print('Number is not divisible by 0 !')
    else:
        return num1/num2
    
num1 = input('Enter the number1 : ')
num2 = input('Enter the number2 : ')

try:
    num1 = int(num1)
    num2 = int(num2)
    res = division(num1, num2)
    if res:
        print(res)
except ValueError :
    print('Invalid value !...')

    
