# 24. Write a python script to copy files from a directory D1 based on timestamp(current_date)
# to another directory D2 and delete the source directory D1. Whenever the script is called
# this program must run.

import os
import shutil
import datetime

D1 = ".\\D1\\"
D2 = ".\\D2\\"


for filename in os.listdir(D1):
    src_filepath = os.path.join(D1, filename)
    des_filepath = os.path.join(D2, filename)

    # os.rename(src_filepath, des_filepath)
    shutil.copy2(src_filepath, des_filepath)

# os.rmdir(D1)
shutil.rmtree(D1)


# to get the time-stamp of the file

modified_time = os.path.getmtime(des_filepath) # it returns unix time that measured in seconds

print(modified_time) 

date_time = datetime.datetime.timestamp(modified_time) # it returns the date-time object

print(date_time)

