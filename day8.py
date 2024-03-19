eg : 3
#def profile(name, age, place):
#    txt = 'my name is {}. iam {} years old. iam from {}.'
#    print(txt.format(name, age, place))
#profile("suresh", "22", "nandyal")

# ! Eg:4
# ? Function with return statement

# return
#1.) A variable declared inside the function can be accessed outside the function using return
#2.) return does not print anything
#3.) we cannot write any code below return statement

#def f1():
#    z= 8
#f1()
#print(z) # error ---> cannot use outside the function

#def f1(a, b):
#    c = a*b
#    return c
#print(f1(6, 8))
#obj = f1(6, 8)
#obj1 = f1(4, 6)

#def gracemark(object):
#    print(object+4)
#gracemark(obj)
#gracemark(obj1)

# 123
#def palindrome(n):
#    string = str(n)
#    rev = str(n)[::-1]
#    if string==rev:
#        print(n, "palindrome")
#    else:
#        print("not palindrome")
#a = int(input(" enter the value: "))
#palindrome(a)

# ? Based on the declaration of parameters and args
# ? functions are divided into 6 catagories

#positional args
#keyword args
#default args
#variable length args
#keyword variable length args

# * positional args
# Eg:1
#def profile(name, phone, mark):
#    txt = "my name is {}. my phone number is {}. I got {} marks."
#    print(txt.format(name, phone, mark))#

#profile("suresh", 1234567895, 98) # unexpected output

# * keyword args
# ! EG:1
# ? To overcome the disadvantages of position args, we use keyword args
# ? It is the process of intiating the parameter with the args while callig the function 
#def profile(name, phone, mark):
#    txt = "my name is {}. my phone number is {}. I got {} marks."
#    print(txt.format(name, phone, mark))

#profile(name = "suresh", mark = 98, phone = 1234567895)

# todo ----> Exception of keyword args functions
#def profile(name, phone, mark):
#    txt = "my name is {}. my phone number is {}. I got {} marks."
#    print(txt.format(name, phone, mark))

#profile( name="suresh", 123456789, mark=98)# error ---> positional args follow keywordargs
#profile(1234567895, name="suresh", mark=98)# error---> name has multiple values
#profile("suresh", mark=98, phone=1234567895)
  
# * Defaultargs
# The method of assigning the arguments to the parameter while declaring the function
# ! Eg:1
#def profile(name, phone, place):
#    txt = "my name is {}. my phone number is {}. I am from {}."
#    print(txt.format(name, phone, place))

#profile("suresh", 1234567895)

# ! Eg:2
#def profile(name, phone, place="kadapa"):
#    txt = "my name is {}. my phone number is {}. I am from {}."
#    print(txt.format(name, phone, place))

#profile("suresh", 1234567895, "Guntur")

#def profile(name, phone, place="kadapa"):
#    if place== "Kadapa" or place=="KADAPA" or place=="kadapa":
#       txt = "my name is {}. my phone number is {}. I am from {}."
#       print(txt.format(name, phone, place))
#    else:
#        print("You are not eligible to signup")
#profile("suresh", 1234567895)

# ! Exception
#def profile(name, place="kadapa",phone): # error---> coz default args should not
#    
#    if place== "Kadapa" or place=="KADAPA" or place=="kadapa":
#       txt = "my name is {}. my phone number is {}. I am from {}."
#       print(txt.format(name, phone, place))
#    else:
#        print("You are not eligible to signup")
#profile("suresh", 1234567895)

# * variable length params
# ! Eg:1

#to pass more than 1 arg to a parameter means we use variable length args
#To convert normal parameter to variable length param, add * to the prefix of param

# name = "suri", "name2", "name3"
#def profile(*name):
#    for val in name:
#        print("my name is", val)
#profile("suri", "name2", "name3")

#def profile(*name):
#    for val in name:
#        print("my name is", val, "myt age is", age)
#profile("suri", "name2", "name3", 28) # error --> age has no args

#def profile(age, *name):
#    for val in name:
#        print("my name is", val, "my age is", age)
#profile(28, "suri", "name2", "name3")

# * keyword variable length args

# ! Eg:1

#def price(**price_list):
#    print(price_list)

#price(shirt=1000, iphone=80000)

#d1 = {"a":100, "b":200, "c":300}
#d2 = dict(a=100, b=200, c=300)
#print(d1)

#n = 5
#{1:1, 2:4, 

#n = int(input("Enter the number: "))
#d1 = {}
#for val in range(1, n+1):
#    d1[val] = val**2
#print(5)

#def dict1(n):
#   d1 = {}
#    for val in range(1, n+1):
#        d1[val] = val**2
#    print(d1)
#print(55)

# ! ----> object oriented programming
#The pandigms of objects oriented programming are

#class 
#objects
#inheritance
#polymorphism
#abstraction
#encapsulation

# ! class is a blue print of an object

# l1 = [1, 2, 3, 4, 5, 6]

#? Eg:1
#class c1:
#    name1 = "suri"
#    print(name1)

# Eg:2
#class person:
#    name = "suri"

#c = person() # c is object
#The process of creation of an object is called as Instantiation
#print(c.name)

# ? Eg : 3
#creation of method
#when the function is created with a class is called as method

#class person:
#    def display(person):
#        print("Hello welcome to classes")
#p = person()
#p.display()

#? Eg:4
#class person:
#    def display(person, name, age):
#        print(name, age)

#p = person()
#p.display("suri", 28)


# ? Eg: 5
#class person1:
#    fname = "suri"
#    lname = "T"

#    def first_name(self):
#        print(self.fname)

#    def full_name(self):
#        print(self.fname+" "+self.lname)

#p = person1()
#p.first_name()
#p.full_name()

# Eg:6
# constructor ---> __init__()
# This is a special method which has the ability to execute itself without callking
#it manullay through the process of instantiation
class profile:
    def __init__(self): # constructor method
        print("Hey")

p = profile() # execution of constructor throught this process


