# 8. What is the return type of arbitrary positional arguments and arbitrary keyword arguments

# In Python, arbitrary positional arguments and arbitrary keyword arguments are defined using the 
# *args and **kwargs syntax, respectively.

# The return type of *args is a tuple. 

# It contains all the positional arguments passed to the function after the regular arguments have
# been exhausted.

def my_func(a, b, *args):
    print(a, b, args)

my_func(1, 2, 3, 4, 5) # output : 1 2 (3, 4, 5)


# The return type of **kwargs is a dictionary. 

# It contains all the keyword arguments passed to the function after the regular 
# and *args arguments have been exhausted.

def my_func(a, b, **kwargs):
    print(a, b, kwargs)

my_func(1, 2, x=3, y=4, z=5) # output : 1 2 {'x': 3, 'y': 4, 'z': 5}


