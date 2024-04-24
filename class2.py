import time
from datetime import datetime
import flask 
import random

#string formatting
# f string format


#format method
# .format()


name = 'John Doe'
age = 25
amount = 350000.60
timer = int(input("enter a timer in seconds: "))
number = random.randint(1000, 1000000)
my_list = ['cup', 'cap', 'phone']
item = random.choice(my_list)

print ('''Your name is {}, 
You are {} years old,
your balance is ${},
Thank you {}

Date: {}'''.format(name, age, amount, name, datetime.now()))
time.sleep(timer)
print("You just won a sum of ${:,}".format(number))
print(f'you also won a {item}')



# print(f'your name is {name}, You are {age} years old, your balance is ${amount}')



















# "input(s)"
# account = 1000
# amount = float(input("how much do you want to deposit? "))
# new_account = account + amount
# print ("your current balance is: $" + str(new_account))



# data types converter
# str()
# int()
# float()
# bool()

