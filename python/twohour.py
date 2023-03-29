# 18. Write a python program where for every two hours it prints the pattern without using
# sleep function
# **********
# ********
# ******
# ***
# *

import time

while True:
    start_time = int(time.time())
    print(''' *********
 ********
 ******
 ***
 *''')
    end_time = start_time + 10
    while start_time < end_time:
        start_time = int(time.time())