# 22. Write a function is_iterator so that it accepts an iterable and returns True if the given iterable 
# is an iterator. 
# >>> is_iterator(iter([])) True 
# >>> is_iterator([1, 2]) False
from practice2 import count


def is_iterator(iterable):
    p_m = dir(iterable)
    if '__iter__' in p_m and'__next__' in p_m:
        return True
    return False

print(is_iterator(iter([])))
print(is_iterator([1,2,3]))
print(is_iterator('suhas'))
print(is_iterator(iter('suhas')))

obj = count()
print(is_iterator(obj))