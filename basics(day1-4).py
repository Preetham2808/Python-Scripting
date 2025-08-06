a = 2

b= 8
print('it\'s a beautiful day')
print(a+b)
print(a-b)
print(a/b)
print(a%b)
print(a**b)

pi = 3.14

print(f"pi value is: {pi:.1f}")

"""
python
5.upperC)
s.Lower ()
S.strip()
s.lstrip()
○ s.rstrip()
○ s.replace()
○ s.split()
s.find("python")
s.index(<"string_inp">)
○ s.join()
○ . format()
○ len(s)


B upper / lower
S
'python"


print("Upper: ",s.upper
print("Upper: ";s.lower )
print(s[1:4])
print("Lenght of string:


Len(s))
"""
text = "Hello world python"
replace = text.replace("Hello","hi")
print(replace)

text1 = "Hello,world,python"

split = text1.split(",")
print(split)

find = text.find("world")
print(find)

#index

index = text.index("world")
print("index of world in text variable is", index)

#split method will return list from string

text = "hello,world,python"
split_result=text.split(",")
print("split with ,",split_result) #result we get is list of words seperated with comma(,) in text string

#join method will join a list to a string of words

join_result = ",".join(split_result)
print(join_result)

#checking variable types using type method
x = 22
y ='hello'
z = 3.14
a = [1,2,3]
b = {"key1":"value"}

print("integer",type(x))
print("integer",type(y))
print("integer",type(z))
print("integer",type(a))
print("integer",type(b))

###########################################
##############Data Structure###############

#list

# mutable and ordered collection of different type of member's


#0 Mutable #-> they can be modified during run time

#o undered gives output inorder
#o it supports diff. type of data type's as members
#o storing test case_results
#creating a list

my_list = [1,2,3,'hello',3.14]

#modifying a list

my_list[1] = "python"

#appending a value in list

my_list.append("new")

#removing a value in list

my_list.remove("hello")

print(my_list)


squares = [i**2 for i in range(5)]
print(squares)

#concatination of lists

new_list = my_list + squares

print(new_list)


#dictionary

#creating a dict

my_dict = { "car" : "sedans",
        "honda" : "accord",
        "toyota" : "camry"
        }

print(my_dict)

#adding a key value pair

my_dict["mazda"] = "cx30"
print(my_dict)

#delete a key value pair

del my_dict["mazda"]

print(my_dict)


#iterating in dict
"""
data = {}
size = int(input("enter a size of dict in int"))

for i in range(size):
    key = input("enter a key")
    value = input("enter a value")
    data[key] = value
    print("updated data: ",data)

"""


#dictionaries with touples


dict_with_touple = {'point1': (1,2),
        'point2': (3,4),
        'point3': (5,6)
        }

point1 = dict_with_touple['point1']
print("dict_with_touple",point1)  # we get output of 1 

#sets
"""
⁃ sets are unordered, unique items 
- wont allow duplicate elements 
- sets will support ○ union ->  returns common values 
                    o intersection -> unique values of both sets
                    o difference e.g., (setl set2) it return unique elements in set1
"""
#creating a set

my_set = {1,2,3,"a","b","c"}

#adding a value to a set

my_set.add(5)

#remove a value from a set

my_set.remove(2)

for i in my_set:
    print(f"my_set[{i}]") #interpolation
#    print("elements in my_set",i)

print("my_set: ",my_set)

set1 = {1,2,3}

set2 = {3,4,5}

#union

union = set1 | set2 # gives output of all the values in both the sets
print("union",union) 

#intersection

intersection = set1 & set2 # gives output of common values in both the sets
print("intersection",intersection)

#difference

difference = set1 - set2 #gives output as unique values in set1
print("difference",difference)

#symmetric difference

symmetric = set1 ^ set2 #gives output as (set1 | set2) - (set1 & set2) union - intersection
print("symmentric",symmetric)
