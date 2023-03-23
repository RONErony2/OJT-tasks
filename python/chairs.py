# 27. Need to find minimum number of new chair purchase for work area with simulated set of array
# values.
# C - A new employee comes to work area and new chair need to purchase
# R - Employee from work area goes to meeting room and free up the chair
# U - Employee comes from meeting room and occupy the chair
# L - Leaves the work area and free up the chair
# Input :
# n = 3
# simulated value : ['CCRLU', 'CRLCUC', 'CCCC']
# Output:
# 2
# 2
# 4

def find_minimum_chairs(val):
    available_chairs = 0
    seats_required = 0
    dict_ = {'C':1, 'R':-1, 'U':1, 'L':-1}
    for v in val:
        if dict_[v] == 1:
            if available_chairs > 0:
                available_chairs -= 1
            else:
                seats_required += 1
        else:
            available_chairs += 1
    return seats_required

n = int(input("Enter the number : "))
simulated_val = []
for i in range(n):
    simulated_val.append(input("Enter the simulated value : "))

for v in simulated_val:
    print(find_minimum_chairs(v))