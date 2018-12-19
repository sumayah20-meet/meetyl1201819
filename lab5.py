#import tkinter as tk
#from tkinter import simpledialog
#Then when ever you want to ask the user for input use this code
#greeting = simpledialog.askstring("Input", "Hello possible pirate! What's the password?", parent=tk.Tk().withdraw())
#if greeting in ["Arrr!"]:
	#print("Go away, pirate.")
#else:
	#print("Greetings, hater of pirates!")
#import tkinter as tk
#from tkinter import simpledialog

#year = int(simpledialog.askstring("Input", "Greetings! What is your year of origin?", parent=tk.Tk().withdraw()))

#if year <= 1900:
   # print ("Woah, that's the past!")
#elif year > 1900 and year < 2020:
   # print ("That's totally the present!")
#else:
   #
   # print ("Far out, that's the future!!")
'''
   class Person:
  def __init__(self, first_name, last_name):
    self.first = first_name
    self.last = last_name
  def speak(self):
  	print("My name is " + self.first+ self.last)

me =Person("Brandon", "Walsh")
you =Person("Ethan", "Reed")

me.speak()
you.speak()
'''
'''
exam_one = int(simpledialog.askstring("Input", "Input exam grade one: ", parent=tk.Tk().withdraw()))

exam_two = int(simpledialog.askstring("Input", "Input exam grade two: ", parent=tk.Tk().withdraw()))

exam_three = int(simpledialog.askstring("Input", "Input exam grade three: ", parent=tk.Tk().withdraw()))

grades = [exam_one ,exam_two,exam_three]
sum = 0
for grade in grade:
  sum = sum + grade

avg = sum / len(grdes)

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:


    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C"
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
elif avg <= 0 and avg >= 50: 
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))

    print("Average: " + str(avg))

    print("Grade: " + letter_grade)

if letter-grade is "F":
    print ("Student is failing.")
else:
    print ("Student is passing.")

'''
'''
class Person():
   def __init__(self, name, favorite_food,age):
       self.name = name
       self.fav_food = favorite_food
       self.age = age


   def define_color(self, color="Red"):
       self.color = color

   def print_info(self):
       print("My name is " + self.name + ", I'm " + str(self.age) + " years old.")
       print("My favorite food is " + self.fav_food + " and my favorite color is " + self.color)


a = Person("Britney", "Pizza", 16)
a.define_color("Black")
a.print_info()

a = Person("Jake", 15)
a=define_age(15)
b.print_info()
'''
'''
class Bear():
def __init__(self, name):
self.name = name
print("A new bear created. Its name is: " + self.name)
def say_hi(self):
print("Hi! I’m a bear. My name is " + self.name)
my_bear = Bear("Danny")
my_bear.say_hi()

balloons = 5
name = "Ron"
color = "Yellow"
print("This is a tale about " + str(balloons) + " balloons. The first
kid is " + name + " who got a " + color + "balloon")

class Cake():
def __init__(self,cake_flavor):
self.cake_flavor = cake_flavor

def eat(self):
print("Yummy!!! Eating a " + self.cake_flavor + " cake :)")

cake = Cake("chocolate")
cake.eat()
# what I want to be printed: Yummy!!! Eating a chocolate cake :)
'''
'''class Cat(object):
"""docstring for Cat"""
def __init__(self, name):
self.name = name
def birthday(self):
age=0
for age in range(8):
age+=1
if age >= 100:
print("Dong dong , the cat is dead!")
else:
print(self.name + "is hasing its" + str(age)+ "birthday!" )

my_cat = Cat("Salem")
my_cat.birthday()
# what I want: my cat to celebrate its 8th birthday (and all the
# birthdays that come before that)
'''
'''
class Cake(object):
def __init__(self,flavor):
self.cake_flavor = flavor
def eat(self):
print("Yummy!!! Eating a"+ self.cake_flavor + "cake :)")

a=Cake("Chocolate")
a.eat()
class Cat():
  def __init__(self,name,age):
    self.name = name
    self.age = age
  def birthday(self):
    self.age += 1
    if self.age >= 100
print("Dong dong, the cat is dead!")
else:
print(self.name + "hasing its" + self.age + "birthday!")

my_cat = Cat("Salem")
my_cat.birthday(8)
# what I want: my cat to celebrate its 8th birthday (and all the
# birthdays that come before that)
class Cat(object):
"""docstring for Cat"""
def __init__(self, name):
self.name = name
def birthday(self):
age=0
for age in range(8):
age+=1
if age >= 100:
print("Dong dong , the cat is dead!")
else:
print(self.name + "is hasing its" + str(age)+ "birthday!" )

my_cat = Cat("Salem")
my_cat.birthday()
# whaclass Cat(object):
"""docstring for Cat"""
def __init__(self, name):
self.name = name
def birthday(self):
age=0
for age in range(8):
age+=1
if age >= 100:
print("Dong dong , the cat is dead!")
else:
print(self.name + "is hasing its" + str(age)+ "birthday!" )

my_cat = Cat("Salem")
my_cat.birthday()
# what I want: my cat to celebrate its 8th birthday (and all the
# birthdays that come before that)
'''

# what I want: my cat to celebrate its 8th birthday (and all the
# birthdays that come before that)
'''
class Cake(object):
def __init__(self,flavor):
self.cake_flavor = flavor
def eat(self):
print("Yummy!!! Eating a"+ self.cake_flavor + "cake :)")

a=Cake("Chocolate")
a.eat()a=Cake("Chocolate")
  a.eat()t I want: my cat to celebrate its 8th birthday (and all the
# birthdays that come before that)
'''
class Cake(object):
  def __init__(self,flavor):
    self.cake_flavor = flavor
  def eat(self):
    print("Yummy!!! Eating a"+ self.cake_flavor + "cake :)")

a=Cake("Chocolate")
a.eat()


