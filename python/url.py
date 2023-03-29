# 22.Define the logic for verifying whether URL is Valid or Invalid Requirements for Valid URL
# •Should not contain any Special characters [,*,&,%,$,#,@,!] and Spaces
# •Should start with https://
# Input : URLs will be stored inside a file , read the URLs from the input file [input.txt]
# Output : Generate a .txt file which contains the information whether URL is valid or not
# ( URL, Status [valid/invalid])
# Example:
# Input
# Input.txt [text file]
# https://m 
# http s://m
# Output:
# 1.https://m, valid
# 2.http s://m, invalid

# Note: Define the logic with different approaches [1. Using RegEx 2. Without RegEx]

# with regex
import re

with open("input.txt", "r") as input_file:
    with open("output.txt", "w") as output_file:
        slno = 1
        for url in input_file.readlines():
            match = re.search(r"^https://[\w./]+[\n]?", url)
            if match != None:
                if match.group() == url:
                    output_file.write(str(slno) + ". "  + url.strip("\n")+", valid\n")
                else:
                    output_file.write(str(slno) + ". " + url.strip("\n")+", invalid\n")
            slno += 1


# without regex
with open("input.txt", "r") as input_file:
    with open("output.txt", "w") as output_file:
        slno = 1
        for url in input_file.readlines():
            url = url.strip('\n')
            res = True
            if url.startswith("https://"):
                for i in ["*", "&", "%", "$", "#", "@", "!"]:
                        if i in url:
                            res = False
                            break
            else:
                 res = False
            if res:
                output_file.write(f"{slno}. {url}, valid\n")
            else:
                output_file.write(f"{slno}. {url}, invalid\n")
            slno += 1
