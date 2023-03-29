# 8. Write a function in Python that accepts a credit card number. 
# It should return a string where all the characters are hidden with an asterisk except the last four. 
# For eg., if the credit card no. is “4509876278910046”, then function should return “************0046”.

def hide_credit_card_num(card_num):
    if len(card_num) < 4:
        print("Enter the proper card number")
    else:
        res = "*"*(len(card_num)-4) + card_num[-4:]
        print(res)

card_num = input("Enter the credit card number : ")

hide_credit_card_num(card_num)