
'''#d1 = {'ten':10, 'twenty':20, 'thirty':30}
#d2 = {'thirty':30, 'fourty':40, 'fifty':50}
#d1.update(d2)
#print(d1)

set1 = {'python', 'java', 'data science'}
set2 = {'ML', 'AI', 'R Language', 'python'}
set3 = {'Data Analytics', 'Robotics', 'Deep Learning'}
c =0
flag = 0
for val in range(3):
    c=c+1
    if c==1:
        for val in set1:
            if val in set2 or val in set3:
                flag=1
                break
    if c==2:
        for val in set2:
            if val in set1 or val in set3:
                flag=1
                break
    if c==3:
        for val in set3:
            if val in set2 or val in set1:
                flag=1
                break
if flag==0:
    print('Disjoint')
else:
    print('joint')
    '''
#3.
#list1 = ["M", "na", "i", "Ke"]
#list2 = ["y", "me", "s", "lly"]
#l3 = []
#for i in range(len(list1)):
#    ans = list1[i] + list2[i]
#    l3.append(ans)
#print(l3)

#i=0
#while i<len(list1):
#    l3.append(list1[i]+list2[i])
#    i+=1
#print(l3)

# ! Functions
#? DEF
# function  is a block of code which is  used to perform a specfic functionality
# Function can be created using def keyword

#?  function declaration
#function defination
#function call

# ! eg:
#def greet():# function defination
#    print("Greetings user||")

#greet()
#greet()
#greet()
#greet()
#greet()
#greet()
#greet()
#greet()
#greet() # function calling

# ! Eg:2
#def adding():
#    a = int(input())
#    b = int(input())
#    c = int(input())
#    d = a+b+c
#    print(d)
#adding()
#adding()

#def greeting(name):
#    print('welcome', name)

#greeting("suresh")
#greeting("s--p-y")
#for val in range(3):
#    username = input('enter the name: ')
#    greeting(username) # username is argument
    
#!Eg:3
def profile(name, age, place):
        print(name, age, place)
profile("suresh", "22", "nandyal")

# 1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings

# # s1 = "Hello how are you"
# s2 = "Hello how is"

# 3.)Wrire a code print the 8th fibanochi number
