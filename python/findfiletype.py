# 24.Define a logic for identifying the different files (In different format:.csv, .txt) 
# which are part of a directory
# Input : You can create a directory and create the files with two different formats 
# (Manually for the input)
# Output : Create two different directories and store this files separately based on the extension
# Example :
# Input:
# Assume file1.csv, file2.txt, file3.csv, file4.txt are present inside a directory (Any name)
# Output:

# CSV - [Directory with the name CSV] file1.csv

# file3.csv
# TXT - [Directory with the name TXT] file4.txt
# fiIe2.txt

import os

input_dir = "./python/abc/"
output_dir_csv = "./python/CSV/"
output_dir_txt = "./python/TXT/"


files = os.listdir(input_dir)

if not os.path.isdir(output_dir_csv):
            os.mkdir(output_dir_csv)

if not os.path.isdir(output_dir_txt):
            os.mkdir(output_dir_txt)

for file in files:
    src_file_path = input_dir+file
    if file.endswith(".csv"):
        des_file_path = output_dir_csv+file
        os.rename(src_file_path, des_file_path)
    elif file.endswith(".txt"):
        des_file_path = output_dir_txt+file  
        os.rename(src_file_path, des_file_path)

        
