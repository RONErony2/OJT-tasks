# 9. Given a string "abcde", Display the output as "a1b2c3d4e5"

# 1st approach
string = input("Enter the string : ").lower()

alpa = {'a':'1', 'b':'2', 'c':'3', 'd':'4', 'e':'5', 'f':'6', 'g':'7', 'h':'8', 'i':'9', 'j':'10',
         'k':'11', 'l':'12', 'm':'13', 'n':'14', 'o':'15', 'p':'16', 'q':'17', 'r':'18', 's':'19',
         't':'20', 'u':'21', 'v':'22', 'w':'23', 'x':'24', 'y':'25', 'z':'26'}

res = ""
for char in string:
    res += char+alpa[char]

print(res)

# 2nd approach

string = input("Enter the string : ").lower()

val = ord('a')

res = ""
for char in string:
    res += char+str((ord(char)%val)+1)
 
print(res)