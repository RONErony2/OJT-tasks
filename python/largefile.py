# 21. How do you open a file of large size, say around 10GB? So that program should not
# crash

#1st approach
import os
import time

def read_large_file(file_path):
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(100)  # Read 100B at a time
            if not data:
                break
            yield data  

#  to check the file size
file_size_bytes = os.path.getsize("1GB.bin")
print(file_size_bytes)

for  piece_of_bytes in read_large_file("1GB.bin"):
    time.sleep(1)
    print(piece_of_bytes)


