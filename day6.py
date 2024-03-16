# assesment
# 1.) Python program to capitalize the first and last character of each 
# word in a string
# 2.) Input : 128
# Output : Yes
# 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# 3.)l1=[1,2,3,4], l2=[5,6,7,8]
# Add both l1 and l2, ans=[6, 8, 10, 12]

# Q.1
#s1 = 'what happen'
#fst = s1[0].upper()
#lst = s1[-1].upper()
#print(fst+s1[1:len(s1)-1]+lst)

#print(s1.replace("h", "H"))
#print(s1.capitalize())

#Q.2
#n = 128
#i = 0
#while n!=0:
#    rem = n%10
#    print(rem)
#    n=n//10

#n = 128
#for i in str(n):
#    print(i)

#n = 128
#temp = n
#f1 = 0
#while n!=0:
#    rem = n%10
#    check = temp % rem
#    if check!=0:
#        f1 = 1
#    n=n//10

#if f1==0:
#    print("Yes")
#else:
#    print("no")

#l1 = [8, 9, 0, 7]
#l2 = [7, 6, 5, 4]
#l3 = []

#print(l1[0]+l2[0], l1[0]+l2[1])

#for val in range(len(l1)):
#    ans = l1[val]+l2[val]
#    13.append(ans)
#print(l3)

# !---->

# ? characteristics of set
#1.) set can be created using {}
#2.) the elements inside set are not indexed
#3.) does not allow duplicate values
#4.) it unordered
#5.) heterogenous --> acceot only unmutable datatype
#6.) mutable or changable

# Eg:1
#s1 = {9, 9, 89, 7.76, 8+7j, (8, 7, 5), "truck", 'e'}
#print(s1)

# Eg:2
#s2 = {5, 8, 98, [9, 0]}
#print(s2) #---> error

# Eg:3
#min(), max(), len()

#Eg:4
# ? to add element inside set

#s1  = {8, 78, 67, "u"}
#add()
#s1.add(43)
#print(s1)

#update()
#s1.update([9, 0])
#print(s1)

# ? To delet element inside set
#s1 = {8, 78, 67, 'u'}
#s1.pop()
#print(s1)

# remove
#s1 = {8, 78, 67, 'u'}
#s1.remove(78)
#print(s1)

# discard()
#s1 = {8, 78, 67, 'u'}
#s1.discard(867)
#print(s1)

# clear()
#l1 = {}
#print(type(l1)) #---> datatype is dict

#s1 = set() # to creat empty set
#print(type(s1))

#s1 = {8, 9, 0}
#s1.clear()
#print(s1)

#del s1
#print(s1)

# * join sets
#s1 = {9, 0, 8}
#s2 = {9.90, "card", "t", 56}
# union()---> to combine 2 sets
#s3 = s1.union(s2)
#print(s3)

# intersection() --> to get common elements inside set
#s1 = {4, 5, 6}
#s2 = {5, 6, 7, 8}
#print(s1.intersection(s2))

# * difference()
#s1 = {4, 5, 6}
#s2 = {5, 6, 7, 8}
#print(s1.difference(s2))
#print(s2.difference(s1))
#print(s1.symmetric_difference(s2))

# isdisjoint(), issubset(), issuperset()
s1 = {4, 5, 6}
s2 = {4, 5, 6, 7, 8}
print(s1.issubset(s2))
print(s1.issuperset(s2))

s1 = {4, 5, 6}
s2 = {4, 5, 6, 7, 8}

# n1 = {1, 2, 3}

#for val in s1:
#    ifval in s2:
#        str1 = "its joint set"
#print(str1)

# !----> dictionary
#eg:1
'''
d1 = {1:100, "a":200, 4.5:"hello"}
print(d1)

mech_name =["name1", "name2", "name"]
mech_age = [23, 22, 24]
mech_mark = [89, 78, 60]


d1 = {1:100, "a":200, 4.5:"hello"}
marks_stud1 = "english": 79, "maths":20,
               Eg:1
# d1 = {1:100, 'a':200, 4.5:"hello"}
# print(d1)
# print(len(d1))
'''
# ? char of dictionary
# 1.) have to be surrounded by {}
# 2.) it have to be in the form of key, value pair
# 3.) it is mutable
# 4.) duplicate keys are not allowed, duplicates values are allowed
# 5.) it is unindexed
# 6.) it is ordered
# 7.) key does not allow mutable datatypes, values allow mutable datatype

# d1 = {1:100, 2:200, 3:300, 4:400}
# * to access elements in dictionary
# print(d1)
# or
# to access the values, have to use key
# print(d1[1])# o/p --> 100

# ? some common functions
# len(), min, max()
# print(min(d1))
# print(max(d1))

# ? to find min, max based on values
# print(min(d1.values()))
# print(max(d1.values()))

# ? dictionary based functions
# to add element(key and value pair) in dict
# d1 = {1:100, 2:200, 3:300, 4:400}
# d1[5] = 500
# print(d1)

# ? to replace avalue in dictionary
# d1 = {1:100, 2:200, 3:300, 4:400}
# d1[2]="mango"
# print(d1)

# ? delete element from dictionary
# d1 = {1:100, 2:200, 3:300, 4:400}
# popitem() # --> to delete last key value pair in dict
# d1.popitem()
# print(d1)

# pop()
# d1.pop(2) # 2 is the key in dictionary
# print(d1)

# clear(), del

# join 2 dictionaries
# d1 = {1:100, 2:200, 3:300, 4:400}
# d2 = {"a":"apple", "b":"boy", "g":"game"}
# d1.update(d2)
# print(d1)

# get()
# d1 = {1:100, 2:200, 3:300, 4:400}
# print(d1[3])
# print(d1.get(3))

# to print all the keys()
# print(d1.keys())
# print(type(d1.keys()))

# to print all the values
# print(d1.values())

# * iterating dictionary
# for val in d1: # to iterate keys alone
#     print(val)

# for val in d1.values(): # to iterate values alone
#     print(val)

# to get both key and values
# for key, val in d1.items():
#     print(key, val)

# !-------> problem:1

#n = int(input("Enetr num of times: "))
#integer=[]
#float_value = []
#string=[]

#for val in range(n):
#    value = eval(input("Enter the values: "))
#    if type(value)==int:
#               integer.append(value)
#    elif type(value) == float:
#        float_value.append(value)
#    elif type(value) == str:
#        string.append(value)
#    else:
#        print("pls provide data in int, float, string")
#print(integer)
#print(float_value)
#print(string)

# problem---->2
# Return a set of elements present in Set A or B, but not both
'''
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# o/p
# {20, 70, 10, 60}
set3 = set()
for val in set1:
    if val not in set2:
        set3.add(val)
for val in set2:
    if val not in set1:
        set3.add(val)
        
print(set3)
'''

# ! ---> problem 3
l1 = [1, 2, 3, 4,] # key
l2 = ["a", "b", "c", "d"] # value
# o/p ---> {1:"a", 2:"b", 3:"c", 4:"d"}
#l3 ={}
#print(l1[0],l2[0])

d1={}
d1[l1[0]] = l2[0]
d1[l1[1]] = l2[1]

d1 ={}
for val in range(len(l1)):
    d1[l1[val]] = l2[val]
print(d1)
print(d1)

# ----> Assesment
# 1.) dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# Merge two python dictionary
# o/p --> {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# 2.)Python Program to determine if 
# the given Sets Are Disjoint 
# or Not without Using Inbuilt-in Functions

# set1 = {'Python', 'Java', 'Data Science'}
# set2 = {'ML', 'AI', 'R Language', 'Python'}
# set3 = {'Data Analytics', 'Robotics', 'Deep Learning'}

# 3.)list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]

# O/P --> ['My', 'name', 'is', 'Kelly']

