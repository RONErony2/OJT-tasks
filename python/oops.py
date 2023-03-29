# 8. Write Row class that accepts any keyword arguments given to it and stores these arguments as attributes.
# Ex. >>> row = Row(a=1, b=2)

# >>> row.a

# 1

# >>> row.b

# 2

#1st approach
class Row:
    def __init__(self,**kwargs):
        for k,v in kwargs.items():
            setattr(self, k, v)

row = Row(a=10, b=20, c='suhas')

print(row.a)

# 2nd approach
class Row:
    def __init__(self,**kwargs):
        self.__dict__.update(kwargs)

row = Row(a=10, b=20, c='suhas')

print(row.a)