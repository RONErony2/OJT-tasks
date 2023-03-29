# 15. Create a new dictionary using the list and dictionary defined below. 
# The keys of the new dictionary will be the elements in the list so we will iterate over 
# the elements in list. If the element is also in the dictionary, the value will be the values 
# of that key in the dictionary. Otherwise, the value will be the length of the key. 
# I/p: 
# lst = ['data','science','artificial', 'intelligence'] 
# dct = {'data': 5, 'science': 3, 'machine': 1, 'learning': 8} 
# O/p: {'artificial': 10, 'data': 5, 'intelligence': 12, 'science': 3} 

lst = ['data','science','artificial', 'intelligence'] 
dct = {'data': 5, 'science': 3, 'machine': 1, 'learning': 8} 

new_dict = {}

for key in lst:
    if key in dct:
        new_dict[key] = dct[key]
    else:
        new_dict[key] = len(key)

print(new_dict)
