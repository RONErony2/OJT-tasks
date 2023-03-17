# 21. You are given a string and width. Your task is to wrap the string into paragraph of width in
# reverse order. Blank spaces should be ignored.
# for eg: i/p - first line contains a string with blank spaces - Hello, welcome to this organisation.
# the second line conatins the width - 4
# o/p :
# lleH
# ew,o
# mocl
# tote
# osih
# nagr
# tasi
# .noi

def wrap_string(string, width):
    string = string.strip()
    if len(string) == 0 or width == 0 or width > len(string):
        return []
    res = ""
    paragraph = []
    for char in string:
        if char != " ":
            res += char
            if len(res) == width:
                paragraph.append(res[::-1])
                res = ""
    return paragraph

string = input("Enter the string : ")
width = int(input("Enter the width : "))

for para in wrap_string(string, width):
    print(para)
