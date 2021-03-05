from datetime import datetime
import random
import time

odd = [1, 3, 5, 7, 9, 11, 13, 17, 19, 
1, 23, 25, 27, 29, 31, 35, 37, 39, 
41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

timerightnow = datetime.today().minute

for i in range(5):
    if timerightnow in odd:
        print("This minute seems a little odd.")
    else:
        print("Not an odd minute.")
    wait_time = random.randint(1, 60)
    time.sleep(wait_time)

