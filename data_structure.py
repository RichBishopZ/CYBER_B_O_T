# Pythhon data structure

# list
# Dictionaries
# Tuples
# sets

#1 list

my_list = [1, 2, 3, 4, 5, 6, 7, 8]

word_list = ['get', 'bag', 'cap', 'run']

x = word_list[3]
# print(x)

color= "Red"
xa= [234, "hello", True, 3.234, color, [1, 2, 3, 4, 5, 6, 7, 8]]

# Method in Python lists

# .append method

my_list = [1, 2, 3, 4, 5, 6, 7, 8]
my_list.append('number')
# print (my_list)

# .extend method

x = [1, 2, 3, 4, 5, 6, 7]

y = [8, 9, 10, 11, 12, 13, 14, 15]

x.extend(y)
# print (x)

#.insert method

x = [1, 2, 3, 4, 5, 6, 7]

x.insert(0,0)
# print (x)

# .remove method

x= [1, 2, 3, 4, 5, 6, 7]

x.remove(2)
# print (x)

# .pop method
x = [1, 2, 3, 4, 5, 6, 7]

num = x.pop(2)
# print (x)
# print (num)

# . index method
x = ['a', 'b', 'c', 'd', 'e', 'f']

positions = x.index('c')

# print (positions)


# . count method

x = ['a', 'b', 'c', 'd', 'e', 'f']

positions = x.count('c')
# print (positions)

# .sort method

x = [23, 44, 25, 66, 48, 100, 102,]

# x.sort()
# print(x)

#.reverse method
x = [23, 44, 25, 66, 48, 100, 102,]
x.reverse()
# print(x)

x.sort(reverse=True)
# print(x)


#2 Dictionaries

# word = 'meaning'

# x = {'key' : 'value'}

# x = {'key' : {'valuekey' : 'value', 'valuekey' : 'value'},
#      'key' : 'value',
#      'key' : 'value',
#      'key' : 'value',}

# Car Model Dictionary
car = dict()

# print(car)

car["name"] = "TOYOTA"
car["Brand"] = "Corolla"
car["type"] = "SE"
car["engine_type"] = "6 plug"
car["price"] = 4000000

# print(car.items())

car ["price"] ="#{:,}".format(car["price"] + 1500000)
# print ("#{:,}".format(car["price"]))
# print(car.items())

name = "My name is DANNY BOYARD,"
age = "30 by age,"
sex= "male by gender,"
Class= "and a masters degree student"

# print(name, age, sex, Class)

# student=dict()

# student.items('name', 'age', 'sex', 'Class')

# student['name']= 'DANNY BOYARD'
# student['age']= '30 by age'
# student['sex']= 'male by gender'
# student['Class']= 'and a masters degree student'

# # print(student.items('name', 'age', 'sex', 'class))

# for x in student.items():
#     if x == 'sex':
#         print('females')

name = input('Enter your name')
age = int(input('How old are you: '))
Class = input('What class are you')
gender = input('What gender are you: ')

student =dict()

student['name'] = name
student['age'] = age
student['Class'] = Class
student['gender'] = gender

print(student.items())

for keys, val in student.items():
    print({keys : val})
    




    
