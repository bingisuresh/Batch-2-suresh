# polymorphism in classes
#we can achieve polymorphism in 2 ways
#1.) Method overloading---> it is not possible in python
#2.) Method overloading

# method riding
# polymorphism in classes
'''
# Eg:1
class bank:
    def ratio(self):
        print("All banks has repo rate")

class SBI(bank):
    def ratio(self):
        print("SBI rate is 9%")
        
class IOB(bank):
    def ratio(self):
        print("IOB rate is 7.5%")

i = IOB()
i.ratio()

s = SBI()
s.ratio()
'''
# ? Eg:2
'''
class USA:
    def language(self):
        print("English")

    def capital(self):
        print("Washington DC")

class India(USA):
    def language(self):
        print("None")

    def capital(self):
        print("New delhi")

I = India()
I.language()
I.capital()
'''
# Eg:3
#polymorphism using objects

#c1,c2---> c1 = print(c1), print(c2)
'''
class c1:
    def f1(self):
        print("c1")

class c2(c1):
    def f2(self):
        super().f1()
        print("c2")
        
obj1 = c2()
obj1.f1()

#obj2 = c2()
#obj2.f2()
'''
#Eg:4
'''
class c1:
    def f1(self):
        print("class 1")

class c2(c1):
    def f2(self):
        print("class 2")
        
obj1 = c2()
obj2 = c1()

def display(a):
    a.f1()
display(obj1)
display(obj2)
'''
#changing the functionality of builtin functions
'''
class shooping:
    def __init__(self, l1):
        self.items = l1

    def __len__(self):
        length = len(self.items)
        return length
s = shooping([1,2,3,4,5])
print(len(s))
#print(len(s))

#s.item_list([1,2,3,4,5])
'''
# ! ---> Method overloading
# Eg:1
'''
class suming:
    def add(self, a, b):
        print(a+b)

    def add(self, a, b, c):
        print(a+b+c)

s = suming()
#s.add(4, 3) # !---> error
s.add(4, 5, 1)
'''

# ! Eg:2
'''
class suming:
    def add(self, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            print(a+b+c)
    
        elif a!=None and b!=None:
            print(a+b)
        else:
            print(a)

obj= suming
obj.add(2)
obj.add(3,4)
obj.add(1,2,3)

'''
'''
a = 9
b = 6
#print(a+b)
print(a.__add__(b)) #? dunder method
print(a.__sub__(b))
print(a.__mul__(b)
'''
#! ----> Abstraction
#The process of hiding the implimentation details is abstraction

# Eg:1
'''
from abc import ABC,abstractmethod
class shapes(ABC):
    @abstractmethod
    def sides(self):
        print("All shapes have sides except circle")

class triangle(shapes):
    def triangle_sides(self):
        print("3 sides")

    def name(self):
        print("Iam triangle")

    def sides(self):
        pass

class square(shapes):
    def square(self):
        print("4 sides")

tr = triangle()
tr.triangle_sides()
tr.name()
'''
# ! Rules to define abstract class1
#1.) Abstract class cannot be instantiated
#2.) from abc import ABC, abstractmethod
#3.) subclass the normal class with ABC
#4.) convert the normal method inside the abstract class to abstract method
#5.) All the child classes have to be subclassed with abstract class
#6.) The abstract method should be present in the child classes

# ! Eg:2
# super()
'''
from abc import ABC, abstractmethod
class c1(ABC):
    @abstractmethod
    def m1(self):
        print("this is abstract class")

class c2(c1):
    def m2(self):
        super().m1()
        print("Iam child 1")

    def m1(self):
        pass

class2 = c2()
class2.m2()
'''
# Eg:3
'''
from abc import ABC, abstractmethod
class password(ABC):
    @abstractmethod
    def pwd(self):
        pswd = "suri2001$"

class login:
    def validate(self, name, password):
        if super().pwd() == password:
            print("Welcome", name, '!!')
            print("Login successful")

    def pwd(self):
        pass

Login = login()
name = input(" Enter the name: ")
pwd = input("Enter the password:")
Login.validate(name, pwd)
'''

# ! Encapsulation
# *-----> Eg:1
'''
class car:
    __name = "BMW" # private variable
    print(__name)
c1 = car()
print(c1.name) #error
c1.name = "Audi"
print(c1.name)# error
'''
# Eg:2
#? Accessing private data outside the class
'''
class c1:
    __phone = '7889944556'

    def display(self):
        print(self.__phone)
c = c1()
c.display()
'''
# Eg3
'''
#? declare private method
class class1:
    def __m1(self):
        print("iam private method")

    def __init__(self):
        self.__m1()
c= class1()
#c.__m1() #error
'''
# ? nested class
'''
class class1:
    class class2:
        name = "suri"

        def display(self):
            print(self.name)
    obj1 = class2()

obj = class1()
obj.obj1.display()
'''
 #!----> Tasks
#Write the code for the below tasks using function
#1.) d1 {"shirt": 1000, "pant": 1500, "Shoes": "900", "handkey": 30)
'''
d1 ={"shirt": 1000, "pant": 1500, "Shoes": 900, "handkey": 30}
for val in d1:
    if d1 [val] == min(d1.values()):
        print(val)
for val in d1:
    if d1[val] == max(d1.values()):
        print(val)
for val in d1:
    if val.startswith('s') or val.startswith('S'):
        print(val)
'''
