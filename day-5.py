# Use exception in except than any other specific exception
num = [12,3,4,4,1,3,3]
try:
    for i in range(len(num)):
        num.pop(i)
    print(num)
except:
    print("index out of bounds")

# Handle zeroDivisionError
try:
    n = 0
    if n%2==0:
        print(1/n)
    else:
        print("odd")
except ZeroDivisionError as e:
    print(e)

#  the user to input an integer and raises a ValueError exception if the input is not a valid integer.
def divide_5():
    try:
        n= int(input())
        print(n//5)
    except ValueError as e:
        print(e)
print(divide_5())

# Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
def open_file():
    try:
        f = open("C:\\Users\\deepa\\Desktop\\myfile.txt")
        s = f.readline()
        print(s)
    except FileNotFoundError as e:
        print(e)
print(open_file())
# ArthematicError
def divide(dividend,divisor):
    try:
        return dividend/divisor
    except ArithmeticError as e:
        print(e)
dividend = float(input("divident"))
divisor = float(input("divisor"))
print(divide(dividend,divisor))

#KeyboardInterrupt Error
try:
    n = int(input())
    print(n)
except KeyboardInterrupt:
    print("type input")

#Attribute error
lst = [1,2,3,4]
try:
    lst.popq(2)
    print(lst)
except Exception as e:
    print(e)

import os
print(os.getcwd())
os.chdir("d:\\placement_practice")
print(os.getcwd())
print(os.listdir("d:\\placement_practice"))
#os.mkdir('d:\\placement_practice\\deepak')
print(os.listdir("d:\\placement_practice"))
os.rmdir("d:\\placement_practice\\deepak")
print(os.listdir("d:\\placement_practice"))

#To read the file
loc = 'C:\\Users\\deepa\\Desktop\\myfile.txt'
f = open(loc,encoding="utf8")
print(type(f))
for x in f:
    print(x)
print(type(x))

# To access a image file we have to use PIL{library} and Image{function}
from PIL import Image
img = Image.open("C:\\Users\\deepa\\Pictures\\instagram.png")
print(type(img))
print(img)
img.show()

# While appending the content it will be attached to the already existing content of the file
f = open("C:\\Users\\deepa\\Desktop\\myfile.txt",'+a')
f.write("This is a new line")
f.close()

f = open('C:\\Users\\deepa\\Desktop\\myfile.txt',mode='r',encoding='utf8')
print(f.read())
print("Program completed")
f.close()

# While write operation if file not exist the new file will be created but 
# if not content in the existing file will be erased and re wrote 
f = open('C:\\Users\\deepa\\Desktop\\file.txt','w+')
f.write("this is the content want to be writtened")
print(f.read())
f.close()

# Using with keyword
with open('C:\\Users\\deepa\\Desktop\\file.txt','a+') as file:
    file.write(". The luck favors brave")
    content = file.read()
    print(content)

# Write a  Python program to read first n lines of a file.
with open('C:\\Users\\deepa\\Desktop\\file.txt','r') as file:
    n = int(input("enter the lines: "))
    for i in range(n):
        line = file.readline()
        if line:
            print(line.strip())
        else:
            break

# Write a Python program to read a file line by line and store it into a list.
with open('C:\\Users\\deepa\\Desktop\\file.txt','r') as file:
    last = []
    for x in file:
        line = file.readline()
        last.append(line)
    print(last)

# Longest word in the file
with open('C:\\Users\\deepa\\Desktop\\file.txt','r') as file:
    line = file.read().split()
    max_len = len(max(line,key=len))
    print(max_len)
    max_word = [i for i in line if len(i)==max_len]
    print(max_word)

# Program to count the lines in a file
with open('C:\\Users\\deepa\\Desktop\\file.txt','r') as file:
    for i, l in enumerate(file):
        pass
    print(i+1)

# Program to append the content of file in a list
with open('C:\\Users\\deepa\\Desktop\\file.txt','r') as file:
    lst = []
    for i, l in enumerate(file):
        lst.append(l.strip())
    print(lst)

# Write a Python program to count the frequency of words in a file.
from collections import Counter 
with open('C:\\Users\\deepa\\Desktop\\file.txt','r') as file:
    print(Counter(file.read().strip()))

import shutil 
file = open("C:\\Users\\deepa\\Desktop\\myfile.txt",'rb')
trans = open("D:\\practice\\text.txt",'wb')
shutil.copyfileobj(file,trans)
file.close()
trans.close()

f = open('C:\\Users\\deepa\\Desktop\\myfile.txt',mode='r',encoding='utf8')
print(f.read())
f.close()

import json
dict = {'name':'deepak' ,'details':{'none':None,'grade':2.2}}
print(dict)
json.dumps(dict)
print(dict)

# Opening JSON file in JSON format
import json
with open(r"D:\practice\info.json", mode="r", encoding="utf-8") as read_file:
    frie_data = json.load(read_file)
    
print(type(frie_data))


import os
if os.path.exists('C:\\Users\\deepa\\Desktop\\text.txt'):
    with (open('C:\\Users\\deepa\\Desktop\\text.txt','w'))as file:
        file.write(" This is brave")
    print("Statement executed!!")
else:
    print("it is deleted")

field = []
rows = []
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    fields = next(csvreader)

    for row in csvreader:
        rows.append(row)
    
    # get total number of rows
    print("Total no. of rows: %d" % (csvreader.line_num))

# printing the field names
print('Field names are:' + ', '.join(field for field in fields))
print('\nFirst 5 rows are:\n')
for row in rows[:5]:
    # parsing each column of a row
    for col in row:
        print("%10s" % col, end=" "),
    print('\n')

