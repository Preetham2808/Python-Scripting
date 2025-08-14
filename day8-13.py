#to get file name and directory name seperately, use dirname and basename

directory = os.path.dirname(path)
file_name = os.path.basename(path)

print("this is the directory", directory)
print("this is the file name",file_name)


############### pathlib module #################


from pathlib import Path

path1 = Path("/home/preetham/q1.txt")

# to check whether file exists or not we use exists()
if path1.exists():
    print("file exists")
else:
    print("file not exists")

path2 = Path("/home/preetham/q.txt")
# to check path is absolute or not
if path2.is_absolute():
    print("yes it's absolute path")
else:
    print("not a absolute path")
# to make directory use mkdir()
path3 = Path("/home/preetham/python")
#path3.mkdir()

# to check file or folder

if path3.is_file():
    print("it's a file")
elif path3.is_dir():
    print("it's a directory or folder")


# write text to a file use write_text()
"""
path4 = Path("/home/preetham/python/p1.txt")

path4.write_text("hello python")
"""

# appending text in a file
"""
path5 = Path("/home/preetham/python/p1.txt")

with path5.open("a") as append_handle: # we dont have direct append method we need to open file in append mode and use write() to append lines
    append_handle.write("\nthis line appended using python")
"""
# reading a text in file

path6 = Path("/home/preetham/python/p1.txt")

content = path6.read_text()

print(content)

# path manipulation

#get a file name

print(path6.name) #getting name of the file from path6 path - p1.txt

print(path6.parent) #get directory from file path path6 - /home/preetham/python

print(path6.suffix) # get extension from path6 - .txt

print(path6.stem)  # get only file name without extension name


###############  5. Iterating through files and directories  ###############

# Iterating through directory files
# - path.iterdir(): yields all entries in the directory
# Usage examples:
# - regression logs
# - waveform dump files
# - coverage reports

path9 = Path("/home/preetham/python")

# List all files and directories in the specified path
for file in path9.iterdir():
    print("File:", file)

# Find and list all files with the .txt extension
for txt_file in path9.glob("*.txt"):
    print("Files with *.txt:", txt_file)


### Assignment-2
# create a dir with name "log_files"
#   o sim1.log, sim2.log, sim3.log, sim4.log

# write a script to iterate through directory, list all the file with *.log extension
#   o create absolute paths for each log file

path10 = Path("/home/preetham/python/log_files")

temp_list = []

for log_file in path10.glob("*.log"):
    temp_list.append(log_file)
    print(f"{log_file.parent}/{log_file.name}")
print("this is temp list: ",temp_list)


# shutil

import shutil


#copy contents of p1.txt into p2.txt(it create p2.txt and copy the contents of p1.txt) in python folder

#shutil.rmtree("","") it deletes all the content present in directory note: be sure before use this command as it deletes all the content 

#shutil.copy("/home/preetham/python/p1.txt","/home/preetham/python/p2.txt")


#if you want to get permissions and timestamp of p1.txt to p2.txt then we use shtil.copy2

#shutil.copy2("/home/preetham/python/p1.txt","/home/preetham/python/p2.txt")

#shutil.copytree("","") used to copy whole directory into other directory

#shtil.move("","") used to move file from one directory to other directory

##########
# we use total,used, free = shutil.disk_usage("/") to check the storage
# Check disk space during regression? 
# why? these files may be created and use the storage
  #o sim logs
  #o waveform dmps (.vcs, .fsdb, .wlf)
  #o coverage reports
  #o log_analysisi report

total,used, free = shutil.disk_usage("/")

print(f"total:{total},used:{used},free:{free}")


##############  Walking throughout the directory tree  ################

# os.walk:
#   o root: current directory name
#   o dirs: list dir n current directory
#   o files: list of all files in current directory

# pathlib.Path.rglob():
#   o rglob('*.*'): recursively iterate through all files and directories
#       o '*.*' - match every thing

# os

import os

def walk_directory_tree(root_dir):
    for root, dirs, files in os.walk(root_dir):
        print(f"Current directory: {root}")
        for dir_name in dirs:
            print(f"Directory: {os.path.join(root, dir_name)}")
        for file_name in files:
            print(f"File: {os.path.join(root,file_name)}")

#walk_directory_tree('/home/preetham/python')

# pathlib

from pathlib import Path

def walk_directory_tree(root_dir):
    path = Path(root_dir)
    for item in path.rglob('*'):
        if item.is_dir():
            print(f"Directory: {item}")
        elif item.is_file():
            print(f"File: {item}")
        else:
            print(f"Neither Dir nor File: {item}")


#walk_directory_tree('/mnt/c/Users/DELL/Downloads/PYTHON_Training/python123')

########## Subprocess module ##########
# use running linux commands from from the script
# Subprocess.run() -> for single command
# Subprocess.Popen() -> for running multiple commands in background.

# os.system -> use for running linx commands from the python script

# Running a shell command from script
# os.system()

import os

#os.chdir("/mnt/c/Users/DELL/Downloads/PYTHON_Training/python123")
print("Changed Directory:", os.getcwd())

#os.system("ls -l")

import subprocess

# Subprocess - Running shell command, capturing output

#result = subprocess.run(["ls", "-l"], capture_output=True, text=True)

#print("Command output:", result.stdout)

import subprocess

# Create a folder
#subprocess.run(["mkdir", "New_folder"])

# Change into the folder and list contents
#subprocess.run("cd New_folder && ls", shell=True)

#Automate file search
"""
output = subprocess.run(["find",".","-name","*.py"],capture_output=True, text=True)
print(output.stdout)
"""
# to run multiple file one after another 
"""
command = ["mkdir New_Folder",
        "cd New_Folder && touch t1.txt, t2.txt, t3.txt",
        "ls -l"
        ]

for cmd in command:
    subprocess.run(cmd,shell=True)

"""


# Run commands in parallel/simultaneously
 """   o Popen
        stdout = subprocess.PIPE -> it will capture std output
        stderr = subprocess.PIPE -> capture error

    o .communicate() -> it will wait for process to finish, retrieve the output
    o stdout.decode -> it will convert byte format output to string """

# Run commands in parallel/simultaneously
    #o Popen
        # stdout = subprocess.PIPE -> it will capture std output
        # stderr = subprocess.PIPE -> capture error

        # o .communicate() -> it will wait for process to finish, retrieve the output
        # o stdout.decode -> it will convert byte format output to string
# If you want to check internet connectivity
#ping -c 4 google.com

# List files with human-readable sizes
#ls -lh

# Show disk space usage
#df -h


############## Python Regular Expressions ##############

# Use regular expressions for pattern matching
# - Special characters
# Example use cases:
#   - Log files:
#       UVM_ERROR: file_name, line no...
#       UVM_FATAL:
#   - Simulation queries:
#       What is the simulation for testcase?
#   - Excel data:
#       testcase_name, status, error

# Module: re
import re

# ============================
# 1. Basic Syntax & Meta Characters
# ============================
# Commonly used meta characters:
# (To be filled with specific characters like ., *, ?, ^, $, etc.)


# ===========================
# 1. Basic syntax & Meta characters
# ===========================

# Commonly used meta characters:

# . (dot)      - Matches any character except newline
# ^            - Start of a string
# $            - End of a string
# *            - 0 or more occurrences of preceding character
# +            - 1 or more occurrences
# ?            - 0 or 1 occurrence
# []           - Any character inside brackets
# {}           - Repetition operator
# \            - Escape character
# |            - Alternation (OR)

# Python Code Example
import re

# Match the lines that start with "Error"
log = "Error: Simulation failed \n INFO: Error Test is passed"
pattern = r"^Error"

match = re.findall(pattern, log, re.MULTILINE)

#===========================
#         2. Character classes
#===========================

# []     - define a character set
# [abc]  - matches 'a' or 'b' or 'c'
# [^abc] - matches any character except 'a', 'b', or 'c'
# [0-9]  - matches any digit
# [a-z]  - matches any lowercase letter
# [A-Z]  - matches any uppercase letter

# Matching Memory address (hexadecimal)
"""
log = "Memory address = 0x1Abcf"

pattern = r"0x[0-9A-Fa-f]*"

match = re.findall(pattern, log)

print("Memory address: ", match)
"""


# ============================
# 3. ANCHORS (^, $, \b, \B, \w, \W)
# ============================
# ^ - start of the string
# $ - end of string/line
# \b - matches word boundary
# \B - non-word boundaries
# \w - word characters -> [a-zA-Z0-9]
# \W - non-word characters -> [^a-zA-Z0-9]

#import re
# Extracting words ending with "ed"
"""
log = "Test started, executed, failed, compiled"

pattern = r"\b\w+ed\b"

match = re.findall(pattern, log) """



# ================================
# 4. GROUPING & CAPTURING
# ================================
# (....)
# (?:....)
# \d     - for matching decimal values

import re

# Match time, date, type of error - Error / Fatal / Warning
"""
log = "[2025-02-10 22:20:20] Error: bad virtual interface handle"

pattern = r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] (Error|Fatal|Warning): (.*)"

match = re.search(pattern, log)

if match:
    print("Time: ", match.group(1))
    print("Severity: ", match.group(2))
    print("Message: ", match.group(3))

"""
