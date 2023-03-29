# 6. Read a given file and extract the integers from each line, concatenate all the integers 
# present in the same line and print the sum of all these integers. 
# eg: <File content> He is 32 yrs old and his son is 7 yrs old . 
# She is 27 yrs old and her daughter is 2 yrs old . Output : 599 
# calculation : Integers on Line 1 + Line 2 = 327 + 272 = 599

import re 

with open("int.txt", "r") as file:
    data = file.readlines()
    res = 0 
    for line in data:
        int_list = re.findall(r"\d+", line)
        res += int("".join(int_list))
print(res)

