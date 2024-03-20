
# 1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings

# s1 = "Hello how are you"
# s2 = "Hello how is"

# 3.) Write a code print the 8th fibanochi number
'''

s1 = "Hello how are you"
s2 = "Hello how is

s1 = s1.split(" ")
s2 = s2.split(" ")
for val in s1:
    if val not in s2:
        print(val)

for val in s2:
    if val not in s1:
        print(val)
        

n1 = 0
n2 = 1
ans =0+1 ==1

n1 = 1
n2 = 2
ans = 1+1 ==2

n1 = 2
n2 = 3
ans = 1+2 ==3

n1 = 2
n2 = 3
ans =2+3=5
'''
# find the 8th fibanochi number
#num=8
#n1=0
#n2=1

#for val in range(num):
#    ans=n1+n2
#    n1=n2
#    n2=ans
#print(ans)

# ! constructors
# eg:3
 
#unparametarised constructor
#class profile:
#    def __init__ (self):
#        print("hello world")
#obj =profile()
#obj.__init__()


# eg:3
# * parameterised constructors
#class profile:
#    def __init__(self, id, name, age):
#        print(id, name, age)

#obj = profile(310, "suresh", 23)

# ? Eg:4
#class c1:
#email = "suri@gmail.com"
#    def m1(self):
#        name = "suri"
#        place = "NDL"
#        print(name, place)
#        print(self.email)

#object = c1()
#object.m1()

# ? Eg:5
#class c1:
#    def m1(self):
#        name = "suri"
#        age = 23
#        return name, age
#    def display(self):
        # ! print(name, age)
        # ! print(self.name, self.age)
#        print(self.m1())

#object = c1()
#object.display()

# ? eg:6
#To use the variable inside the constructor in another methods
#class class1:
#    email = "suri@gmail.com"   # static variable
#    def __init__(self):
#        self.name = "suri"      # instance variable
#        self.email = "suri@gmail.com"
        #return name, email #error---> cannot use return with constructor

#    def display(self):  # instance method
#        print(self.name, self.email)

#c1 = class1()
#c1.display()

# ! ------> Inheritance
#The process of utilising the methods and attributes of parent class
#throught the objects of child class it is called as inheritance

# ? 5 types of Inheritance
#single Inheritance
#Multilevel Inheritance
#Multiple Inheritance
#Hybrid Inheritance
#Heirarical Inheritance

# * single Inheritance
#It ha sonly one parent class and only one choild class
# ! Eg :1
#class parent:
#    def m1():
#        print("I am parent class")
#parent.m1()
#class child:
#    def m2():
#        print("Iam child class")
#child.m2()
   # or 
#class parent:
#    def m1(self):
#        print("I am parent class")

#class child(parent):
#    def m2(self):
#        print("Iam child class")

#obj = child()
#obj.m1()

# ! Eg:2
#class c1:
#    def __init__(self):
#        print("Iam constructor from parent class")

#class child(c1):
#    pass

#obj = child()


#Eg:3
#class parent:
#    name = "suri"

#class child(parent):
#    name = "name1"

#    def display(self):
#        print(self.name)

#d = child()
#d.display()

# ! Multilevel inheritance
# ? Eg:1
#class voice:
#    def sound(self):
#        print("All the animals have their own voices")

#class dog(voice):
#    def dog_voice(self):
#        print("bark")

#class cat(dog):
#    def cat_voice(self):
#        print("Meow")

#class parrot(cat):
#    def parrot_voice(self):
#        print("speak")

#all = parrot()
#all.dog_voice()
#all.cat_voice()
#all.sound()
#all.parrot_voice()

# EX:2
'''
class honda_city:
    def engine_specs(self,cc,hp,torque,fuel_type, num_of_piston):
        print(cc, Hp, torque, fuel_type, num_of_piston)
        
    def honda_city_body_specs(self, color, weight, height, length, vehicle_type):
        print(color, weight, height, length, vehicle_type)
        
class amaze(honda_city):
    def amaze_engine_s (parameter_torque, Any , fuel_type, num_of_piston):
        print(cc, Hp, torque, fuel_type, num_of_piston)
        
    def amaze_body_specs(self, color, weight, height, length, vehicle_type):
        print(color, weight, height, length, vehicle_type)
        
class civic(amaze):
    def civic_engine_specs(self, cc, Hp, torque, fuel_type, num_of_piston):
        print(cc, Hp, torque, fuel_type, num_of_piston)
        
    def civic_body_specs (self, color, weight, height, length, vehicle_type):
        print(color, weight, height, length, vehicle_type)
        
class Honda(civic):
    pass

honda =Honda()
honda.honda_city_engine_specs (1500, 230, 2979, "petrol", 4)
honda.civic_body_specs("white", 2000, 5.5, 8, "Hatchback")



 # Multiple Inheritance
 #? It has multiple parent and 1 child
class while_pertol:
    def function_w(self):
        print("used to Airplans")

class Organic_petrol:
    def function_o(self):
        print("used for Bike, cars")
class premium_petrol:
    def function_p(self):
        print("spots cars, bikes")
class petrol(while_pertol, Organic_petrol, premium_petrol):
    def defanition(self):
        print("Petrols types")
p=petrol()
p.defanition()
p.function_o()

# Eg:2
# MRO---> Method resolution Order
class addition:
    def add(self, a, b):
        print(a+b)
    def mul(self,a,b):
        print(a%b)
class subract:
    def sub(self, a, b):
        print(a-b)
class multiply:
    def mul(self, a, b):
        print(a*b)
class division(addition, subract, multiply):
    def div(self, a, b):
        print(a/b)
calc=division()
calc.add(3,4)
calc.mul(4,2)

 # heirarichal Inheritance
 #! Heirarical inheritance
class catagory:
    def weight(self,weight):
        print("weight")
    def display(self,color,taste):
        print(color,taste)
class tomato(catagory):
    def tomato_specs(self):
        color="black"
        taste= "neutral taste"
        self.display(color,taste)
class carrot(catagory):
    def carrot_specs (self):
        color="green"
        taste= "sweet"
        self.display(color,taste)

c=carrot()
c.carrot_specs()
c.weight("30gms")

t=tomato()
t.tomato_spec()
t.weight("20gms")
'''
# hybrid Inheritance
 # The combination of above 4 inheritance is called Hybrid inheritance
#class c1:
#    def m1(self):
#        print("Class1")
#class c2:
#    def m2(self):
#        print("class2")
#class c3:
#    def m3(self):
#        print("Class 3")

#class c4:
#    def m4(self):
#        print("class 4")

#    def m3(self):
#        print("iam m3 from 4")

#class c5:
#    def m5(self):
#        print("Class 4")
#class c6:
#    def m6(self):
#        print("Class 4")


#obj = c6()
#obj.m6()

# ! -------> polymorphism

#poly, many, morph----> form
#function which has the ability to perform more than 1 functionality
#then itb is considered to be as plioymorohism

# * polymorphism in builtin functions
#len()--->which is used to find the length of list, tuple, dict etc....
#index()
#max()
#min()
#count()
#pop()
#and more....

# * polymorphism in operators
# +
print(8+8)
print("k"+"i")
#print[1,2,3]+[5,6]

# *
print(6*7)
l1 = [12,3,4,5,6]
print(*l1)
#def f1(*args)
l1 = [1,2,3,4]
print(l1*10)

# polymorphism in classes
#We can achieve polymorphism in 2 ways
#1.) Method overloading ---> it is not possible in python
#2.) Method overloading















