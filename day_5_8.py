"""
#Fibonacci series using while loop

n = int(input("fibbonacci printer, enter a to number to genrate sequence of fibonacci numbers: "))
a,b = 0,1
count = 0

while count < n:
    print(a, end = " ")
    a,b = b, a + b
    count += 1
print()

#list vs while loop
# find max value in a list using while loop

my_list = [3,5,6,8,9,100,0,101]
#print(len(my_list))
i = 0
j=1
while i < len(my_list):
    if my_list[j] >= my_list[i]:
        max_value = my_list[j]
        i += 1
    else:
        max_value = my_list[i]
        j += 1
print(max_value)

#checking whether a number is prime or not

num = int(input("[prime number ckecker] enter a number: "))

i = 1
list1 = []
while i <= num:
    if num % i == 0:
        print(i)
        list1.append(i)
        i += 1
    else:
        i +=1
if len(list1) == 2 or num ==1:
    print("prime number")
else:
    print("not a prime")

#for loop to get values in dictionary

language_ver = {"py":"3.8","pl":"2.2","sv":"1800"}

for key,value in language_ver.items(): #.items helps to get both key and value from dicts
    print(f"key: {key}, value: {value}")

#for loop in list

cars = ['accord','camry','cx5','k4']

for index,el in enumerate(cars): #to get both index as well as elements in list we can enumerate(list_name)
    print(f"cars_list:{index,el}")

#for loop in tuple

tup = (10,20,30)

for i in tup:
    print("elements in tuple: ",i)

for i in (10,30): #this will return 10,30 becsause it's iterating through only two elements in (10,30) tuple
    print("elements in tuple: ",i)

#for loop in sets

num = {1,2,3,4,4,5,6,6,6}

for i in num: #sets won't give repeated elements and only gives unique values
    print("num_set elements",i)

squares = [i**2 for i in range(5)]
print("squares in list",squares)
square_set = {i**2 for i in range(5)}
print("squares in set",square_set)


# using nested for loop we can print tables

for i in range(1,4):
    for j in range(1,11):
        print(f"{i}*{j} =",i*j)
    print("================")
"""
# find vowel count in a string

text = "hello python"
vowels = "aeiou"
vowel_count =0
for char in text:
    if char in vowels:
        vowel_count +=1
print(f"number of vowels in text: {text} is",vowel_count)

## Functions 
# Defining and calling functions 
             #○ syntax: def  
             #use: to organize the .code into reusable blocks 
             #O it also improves readablity

def fun_name(name):
    print(f"printing name which is given as an argument to this function: {name}")

fun_name("python")

def fun_name(name = "default name is given to this argument"): #this function is overriding the same function (fun_name just declared above) 
    print(f"printing name which is given as an argument to fun_name function: {name}")

fun_name("hi")

def cal_perimeter_area(length,width):
    perimeter = 2*(length+width)
    area = length * width
    return length,width,perimeter,area

length,width,perimeter,area = cal_perimeter_area(2,4)

print(f"length: {length}, width: {width}, perimeter: {perimeter}, area = {area}")


##### variable scope ####

#global - by default variable are global can be accessed by all the functions 

x = 10

def num():
    i=2
    print(f"accessing global variable x inside func: {x}")
    print(f"accessing local variable i inside func: {i}") #local - by default function variables are local cannot be accessed outside function
num()
#local - by default function variables are local cannot be accessed outside function

x = 10

def num():
    global x # if you are using global, nonlocal or local keywords declaration must be done before writing any statement
    x=2
    print(f"accessing global variable x inside func: {x}")
num()

# nonlocal can be using inside nested functions to change global variable (which is in outside function) in inside function


def outside():
    x = 10
    def inside():
        nonlocal x
        x=11
        print(x)
    inside()
    print(x)
outside()

################ FILEHANDLING ################
# Modes of file accessing
#    o "w" - write mode -> overwriting
#    o "r" - read mode -> normal read
#    o "a" - append text to existing file -> No overwriting happened
#    o How to prepend content to a file?
#
# all are create 3 files
#    q.txt
#    q1.txt
#    q2.txt
#
# NOTE: both rd/wr -> each row in a file is considered as index
#    o row0 -> index0,
#    o row1 -> index1, ....so on.

# read contents from q.txt
# to read from q.txt - 1st create file handle then open and then give 'r' which means read

fh_read0 = open("q.txt","r") #open keyword read the file into a list 

fh_write1 = open("q2.txt","w")
"""
for each_line in fh_read0:
    print("each line in q.txt",each_line.strip())
    fh_write1.write(each_line)
"""
#fh_read1 = open("q1.txt","r")
"""
for each_line in fh_read1:
    print("each line in q1.txt",each_line)
    fh_write1.write(each_line)
"""
# Assignment:
# print same row/index content of both files q.txt and q1.txt side by side

# output: q2.txt
# --------------------
# q.txt - row0
# q1.txt - row0
# q.txt - row1
# q1.txt - row1
# q.txt - row2
# q1.txt - row2
# q.txt - row3
# q1.txt - row3

# Answer below
"""
for each_line in fh_read0:
    fh_write1.write(each_line)
    for each_line in fh_read1:
            fh_write1.write(each_line)
            break
#read file line by line
"""
"""
with open("q.txt","r") as fhread:
    line = fhread.readline()
    while line:
        print(line.strip())
        line = fhread.readline()
"""
"""
#read only specific lines of code

with open("q.txt","r") as fhread:
    for line in range(5):
        each_line = fhread.readline()
        if not each_line:
            break
        print(each_line.strip())

with open("q.txt","r") as fhread:
    line = fhread.readlines()
    specific_line = line[2]
    print("this is index 2nd line in q.txt file: ",specific_line.strip())
"""
### Exception handling in file operations #####################
# try-except-finally blocks for handling file operation errors
# o to know the script is exited
# o knowing issue in file opening
#   to show error if we write/read a file which is already in use
###############################################################

# Error cases
# o Reading unexisting file -> script needs to return error
# o File permission error -> writing / reading from protected files

# Handling the file read error
try:
    file = open("q.txt","r")
    content = file.read()
    print(content.strip())
except FileNotFoundError:
    print("file you are tring to read/write is not existing")
except PermissionError:
    print("you don't have the permission to access this file")
except IOError:
    print("no permission to access this file at the moment as it is already in use")
finally:
    print("execution of file is completed")

########### File/Directory path handling from python methods #############
# if we want to execute your script any directory of Linux system
# o script should know complete path to the read/write files
# File Paths: for managing file paths, we have 2 modules in python
# o os.path
# o pathlib

# Absolute path:
# o full path from the root directory
# o e.g., => /mnt/c/Users/DELL/Downloads/PYTHON_Training/q.txt

# Relative path:
# o Path relative to the current working directory
# o e.g., => q.txt

# OS module:
# o provides basic file path operation

# pathlib Module:
# o we prefer - easy to use, its readable

import os


file_name = "q.txt"

cwd = os.getcwd()

fullpath = os.path.join(cwd,file_name) # to join both directory and filename in the path
#print(fullpath)

relative_path = "q1.txt"
absolute_path = os.path.abspath(relative_path) # to get absolute path from relative path
print(absolute_path)


# checking whether given path is absolute or not

#path = "q1.txt"
path = "/home/preetham/q1.txt"

if os.path.isabs(path):
    print(f"{path} is an absolute path")
else:
    print(f"{path} is a relative path")
