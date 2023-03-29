# 12. Write a Python Program to Reverse the Content of a File. 
# Input :- I amnew to this world of Python. 
# Output :- Python. world of new to this I am

with open('./input_file.txt', 'r') as input_file:
    with open('./output_file.txt', 'w') as output_file:
        input_file_content = input_file.readlines()
        for i in range(len(input_file_content)-1, -1, -1):
            output_file.write(input_file_content[i])

