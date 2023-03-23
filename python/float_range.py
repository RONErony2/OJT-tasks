# 21. Write a callable called float_range that acts sort of like the built-in range callable 
# but it should allow for floating point numbers to be specified as start, stop, and step values. 
# >>> r = float_range(0.5, 2.5, 0.5) 
# >>> list(r) [0.5, 1.0, 1.5, 2.0] 
# >>> len(r) 4
# >>> for n in r: ... 
#     print(n) ... 
# o/p : 0.5 1.0 1.5 2.0

def float_range(start,end,step):
    r = len(str(step).split('.')[1])
    result = []
    if step > 0:
        while start < end:
            result.append(start)
            start += step
            start = round(start,r)
    else:
        while start > end:
            result.append(start)
            start += step
            start = round(start,r)
    return result

start = float(input("Enter the start value :"))
end = float(input("Enter the end value :"))
step = float(input("Enter the start value :"))

res = float_range(start,end,step)

print(res)

print("* "*25)

for n in res:
    print(n)

