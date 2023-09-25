### Welcome! This is a Python program file
####
##### The lines that start with a hash (#) are comments
##### They are for you to read and are ignored by Python
####
##### When you see 'GO!', save and run the file to see the output
##### When you see a line starting with # follow the instructions
##### Some lines are python code with a # in front
##### This means they're commented out - remove the # to uncomment
##### Do one challenge at a time, save and run after each one!
####
##### 1. This is the print statement
####
#print("Hello world")
####
###GO!
####
##### 2. This is a variable
####
#message = "Level Two"
#print(message)
#message = 123
#print(message)
#message = 'j'
#print(message)
#message=20.50
#print(message)
#print("message is %0.5f" %message)
##
#print("message is %d" %message)
### Add a line below to print this variable
##
### GO!
##
### 3. The variable above is called a string
### You can use single or double quotes (but must close them)
### You can ask Python what type a variable is. Try uncommenting the next line:
#print(type(message))
### GO!
##
### 4. Another type of variable is an integer (a whole number)
#a = 123
#b = 654
#c = a + b
##
##
### Try printing the value of c below to see the answer
### GO!
##
### 5. You can use other operators like subtract (-) and multiply (*)
### Try some below by replacing the word with the correct operator
##
#a * b
#b - a


#12 - 4
#103 * 999
##
### GO!
##
# 6. Variables keep their value until you change it
##
##a = 100
### print(a)  # think - should this be 123 or 100?
##
##c = 50
### print(c)  # think - should this be 50 or 777?
##
##d = 10 + a - c
##print(d)  # think - what should this be now?
##
### GO!
##
### 7. You can also use '+' to add together two strings
##
greeting = 'Hi '
name = 'NAME'  # enter your name in this string
##
message = greeting + name
#print(message)
##
### GO!
##
### 8. Try adding a number and a string together and you get an error:
##
age =  11
##
#print(name + ' is ' + age + ' years old')
##
### GO!
##
### See the error? You can't mix types like that.
### But see how it tells you which line was the error?
### Now comment out that line so there is no error
##
### 9. We can convert numbers to strings like this:
##
#print(name + ' is ' + str(age) + ' years old')
##
### GO!
##
### No error this time, I hope?
##
### Or we could just make sure we enter it as a string:
##
### age =  # enter your age here, as a string
##
### print(name + ' is ' + age + ' years old')
##
### GO!
##
### No error this time, I hope?
##
### 10. Another variable type is called a boolean
### This means either True or False
##
#raspberry_pi_is_fun = True
#raspberry_pi_is_expensive = False
##
### We can also compare two variables using ==
##
#bobs_age = 15
#your_age =  15
##
#print(your_age == bobs_age)  # this prints either True or False
##
### GO!
##
### 11. We can use less than and greater than too - these are < and >
##
#bob_is_older = bobs_age > your_age
##
#print(bob_is_older)  # do you expect True or False?
##
### GO!
##
### 12. We can ask questions before printing with an if statement
##
money = 250
phone_cost = 240
tablet_cost = 200
##
total_cost = phone_cost + tablet_cost
can_afford_both = money > total_cost
can_afford_phone = money > phone_cost
##
if can_afford_both:
    message = "You have enough money for both"
elif can_afford_phone:
    message = "You can  afford phone "
##
print(message)  # what do you expect to see here?
##
### GO!
##
### Now change the value of tablet_cost to 260 and run it again
### What should the message be this time?
##
### GO!
##
### Is this right? You might need to change the comparison operator to >=
### This means 'greater than or equal to'
##
##raspberry_pi = 25
##pies = 3 * raspberry_pi
##
##total_cost = total_cost + pies
##
##if total_cost <= money:
##    message = "You have enough money for 3 raspberry pies as well"
##else:
##    message = "You can't afford 3 raspberry pies"
##
### print(message)  # what do you expect to see here?
##
### GO!
##
### 13. You can keep many items in a type of variable called a list
##
colours = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
##
### You can check whether a colour is in the list
##
print('Orange' in colours)  # Prints True or False
##
### GO!
print(colours)
##
### You can add to the list with append
##
colours.append('Black')
colours.append('White')
##
print(colours)
print('Black' in colours)  # Should this be different now?
##
### GO!
##
### You can add a list to a list with extend
##
##more_colours = ['Gray', 'Navy', 'Pink']
##
##colours.extend(more_colours)
##
### Try printing the list to see what's in it
##
### GO!
##
### 14. You can add two lists together in to a new list using +
##
primary_colours = ['Red', 'Blue', 'Yellow']
secondary_colours = ['Purple', 'Orange', 'Green']
##
main_colours = primary_colours + secondary_colours
##
### Try printing main_colours
##
### 15. You can find how many there are by using len(your_list). Try it below
##
### How many colours are there in main_colours?
##
### GO!
##
##all_colours = colours + main_colours
##
### How many colours are there in all_colours?
### Do it here. Try to think what you expect before you run it
##
### GO!
##
### Did you get what you expected? If not, why not?
##
### 16. You can make sure you don't have duplicates by adding to a set
##
##even_numbers = [2, 4, 6, 8, 10, 12]
##multiples_of_three = [3, 6, 9, 12]
##
##numbers = even_numbers + multiples_of_three
### print(numbers, len(numbers))
##numbers_set = set(numbers)
### print(numbers_set, len(numbers_set))
##
### GO!
##
##colour_set = set(all_colours)
### How many colours do you expect to be in this time?
### Do you expect the same or not? Think about it first
##
### 17. You can use a loop to look over all the items in a list
##
my_class = ['Sarah', 'Bob', 'Jim', 'Tom', 'Lucy', 'Sophie', 'Liz', 'Ed']
##
### Below is a multi-line comment
### Delete the ''' from before and after to uncomment the block
##

for student in my_class:
    print(student)

##
### Add all the names of people in your group to this list
##
### Remember the difference between append and extend. You can use either.
##
### Now write a loop to print a number (starting from 1) before each name
##
### 18. You can split up a string by index
##
# full_name = 'Dominic Adrian Smith'
# ##
# first_letter = full_name[0]
# last_letter = full_name[19]
# first_three = full_name[:3]  # [0:3 also works]
# last_three = full_name[-3:]  # [17:] and [17:20] also work
# middle = full_name[8:14]
# last = full_name[15:]
# first = full_name[0:7]
# print(full_name)
# print(first)
### Try printing these, and try to make a word out of the individual letters
##
### 19. You can also split the string on a specific character
##
my_sentence = "Hello, my name is Fred"
parts = my_sentence.split(',')
##
#print(parts)
###print(type(parts))  # What type is this variable? What can you do with it?
##
### GO!
##
##my_long_sentence = "This is a very very very very very very long sentence"
##parts = my_long_sentence.split(' ')
###print(parts)
### Now split the sentence and use this to print out the number of words
##
### GO! (Clues below if you're stuck)
##
### Clue: Which character do you split on to separate words?
### Clue: What type is the split variable?
### Clue: What can you do to count these?
##
### 20. You can group data together in a tuple
##
##person = ('Bobby', 26)
##
###print(person[0] + ' is ' + str(person[1]) + ' years old')
##
### GO!
##
### (name, age)
##students = [
##    ('Dave', 12),
##    ('Sophia', 13),
##    ('Sam', 12),
##    ('Kate', 11),
##    ('Daniel', 10)
##]
###print(len(students))
###for i in range(0,5):
###     print(students [i][0] + ' is' + str(students[i][1]) + ' years old ')
##
### Now write a loop to print each of the students' names and age
##
### GO!
##
### 21. Tuples can be any length. The above examples are 2-tuples.
##
### Try making a list of students with (name, age, favourite subject and sport)
##
### Now loop over them printing each one out
##
### Now pick a number (in the students' age range)
### Make the loop only print the students older than that number
##
### GO!
##
### 22. Another useful data structure is a dictionary
##
### Dictionaries contain key-value pairs like an address book maps name
### to number
##
##addresses = {
##    'Lauren': '0161 5673 890',
##    'Amy': '0115 8901 165',
##    'Daniel': '0114 2290 542',
##    'Emergency': '999'
##}
##
### You access dictionary elements by looking them up with the key:
##
###print(addresses['Amy'])
##
### You can check if a key or value exists in a given dictionary:
##
###print('David' in addresses)  # [False]
###print('Daniel' in addresses)  # [True]
###print('999' in addresses)  # [False]
###print('999' in addresses.values())  # [True]
###print(999 in addresses.values())  # [False]
##
### GO!
##
### Note that 999 was entered in to the dictionary as a string, not an integer
##
### Think: what would happen if phone numbers were stored as integers?
##
### Try changing Amy's phone number to a new number
##
### addresses['Amy'] = '0115 236 359'
### print(addresses['Amy'])
##
### GO!
##
### Delete Daniel from the dictinary
##
### print('Daniel' in addresses)  # [True]
### del addresses['Daniel']
### print('Daniel' in addresses)  # [False]
##
### GO!
##
### You can also loop over a dictionary and access its contents:
##
##'''
##for name in addresses:
##    print(name, addresses[name])
##'''
##
### GO!
##
###23 if else
##'''
##a1=12
##if(a1==10):
##    print("a1=10")
##elif(a1==11):
##    print("a1=11")
##else:
##    print("a1 unknown")
##'''
###24 while
##'''
##a2=0
##while(a2<5):
##    print("a is "+str(a2))
##    a2+=1
##'''
###25 input
##'''
##a3=input("Enter a character:")    #everything is read as string
##print(a3)
##'''
###26 Functions in python
####'''
##a4=input("Enter a character:")
##def myfunc():
##    print("hi from myfunc")
##if(a4=='a'):
##    myfunc()
##'''
###27 Parameter passing in Functions in python
####'''
##def square(a5,sq):
##    print("square is "+str(a5*a5))
##    print("square is "+str(sq))
##a4=int(input("Enter num to find square:"))
##square(a4,a4*a4)
####'''
#####28 class
########'''
##class myclass:    #starting letter capital
##    def mess1(self):
##        print("Mess1 from Myclass")
##
##myclass1=myclass()
##myclass1.mess1()
'''
#####29 class with initial value
####'''
##class Employee():
##    def __init__(self,nam,sal):
##        self.nam=nam
##        self.sal=sal
##    def salary(self):
##        print("Salary of "+self.nam+" is Rs."+str(self.sal))
##
##emp1=Employee("paul",1000)
##emp2=Employee("reshma",1200)
##emp1.salary()
##emp2.salary()
##'''
###30 Modules
###create a file called my_module.py
###In it define a function print.hi() to print something
###create a normal print statement outside def to print something
##'''
##import my_module
##my_module.print_hi()
##'''        
###31 Files
'''
##file_ob=open("intro.txt","w")
##file_ob.write("content!")
##file_ob.close()
##'''
##
##'''
##new_ob=open("intro.txt","r")
##content=new_ob.read()
##print("the content of the file : ",content)
##new_ob.close()
##'''  
####
###32 Exception Handling
##'''
##a=int(input("enter a number"))
##try:
##    print("The Result is "+ str(1000/a))
##except ZeroDivisionError:
##    print("calculation not possible")
##finally:
##    print("exit")
##'''
##
###33 Date and time
##
##'''
##import time
##xyz=time.localtime()
##print(xyz)      #time structure
##print(xyz[0])   #year
##print(xyz[3])   #Hour
##'''
##
###34 random numbers
##
##'''
##import random
##print(random.randint(0, 5))
##'''
##
##'''
##import random
##print(random.random())
##'''
##
##'''
##import random
##myList = [2, 109, False, 10, "Lorem", 482, "Ipsum"]
##print(random.choice(myList))
'''
##
##'''
##from random import shuffle
##x=[1,2,3,4]
##shuffle(x)
##print(x)
##'''
##
##'''
##import random
##print(random.randrange(0, 101, 5))
##'''
##
###35 math module
##
##'''
##import math
##y=math.sqrt(4)
##print(y)
##'''
##
###36 Function decorators
###Decorators provide a way to modify functions using other functions. 
###This is ideal when you need to extend the functionality of functions that you don't want to modify.
###We defined a function named decor that has a single parameter func.
###Inside decor, we defined a nested function named wrap.
###The wrap function will print a string, then call func(), and print another string.
###The decor function returns the wrap function as its result.
###In fact, if we wrote a useful decorator we might want to replace print_text with the decorated version altogether so we always got our "plus something" version of print_text
##'''
def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap
##
def print_text():
    print("Hello world!")
##    
###Now print_text is a decorated version of the original print_text function
print_text = decor(print_text)
##
print_text()
##'''
##
###Python provides support to wrap a function in a decorator
###by pre-pending the function definition with a decorator name and the @ symbol. 
###If we are defining a function we can "decorate" it with the @ symbol like:
##'''
def decor(func):
    def wrap():
        print("........")
        func()
        print("........")
    return wrap
##
@decor
def text():
    print("hiii")
##
text()   #This text is a decorated function
##'''
###Now comment the @decor and check the output
##
### Projects
### Project 1
### What is the sum of all the digits in all the numbers from 1 to 1000?
##
### Clue: range(10) => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
### Clue: str(87) => '87'
### Clue: int('9') => 9
##
### Project 2
#####Wrire a program to print the Factorial after taking input from user
##
### Project 3

###Write a program to check wheather a number is Odd or even
####
### Project 4
### Write a program to print the Odd/even nos between user input limits
####
### Project 5
### Write a progarm to print the Fibonnaci series upto a user input limit
    
### Project 6
###Write a program to print the Multiplication table of a user input number

### Project 7
###Write a program to add two Matrix using nested list
##
### Project 8
###Write a progarm to create a simple calculator - using functions and class. +,-,/,*
##
### Project9 
###Write a profram to build an address book - use dictionary
###User should be able to enter - name, housename, district,pincode, phone number.
###Options to store and retrive.
###Clue: Create a blank dictionary first
##
### Project 10
###Write a program to find the area & perimeter. User should be able to input the shape and edges
##
