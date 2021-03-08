# 3 prog to display current date and time

import datetime

now =  datetime.datetime.now()

print("The current date and time is :- ")
print(now.strftime("%y-%m-%d %H:%M:%S"))