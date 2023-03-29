# 21. Write a program that takes one or more filenames as arguments and 
# prints all the lines which are longer than 40 characters. Note :Use generator to solve this question.

def read_line_more_than_40_char(*filePaths):
    for path in file_paths:
        with open(path, "r") as file:
            data = file.readlines()
            for line in data:
                line_length = len(line)
                if line_length > 40:
                    yield line
file_paths = [path for path in input('Enter the space separated file paths : ').split()]

for line in read_line_more_than_40_char(*file_paths):
    print(line, end="")