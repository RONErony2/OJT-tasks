# 21. How do you open a file of large size, say around 10GB? So that program should not
# crash

import time
import os

def read_large_file(file_path, f_size):
    with open(file_path, 'rb') as file:
        current_size = file.tell()
        while current_size != f_size:
            data = file.read(100)  # Read 100 Bytes data at a time
            yield data  
            current_size = file.tell()

#  to check the file size
file_size_bytes = os.path.getsize("1GB.bin")
print(file_size_bytes)


for  piece_of_bytes in read_large_file("1GB.bin", file_size_bytes):
    time.sleep(1)
    print(piece_of_bytes)