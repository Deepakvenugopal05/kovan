
dict = {"a":{"id":123,"name":"raj"},"b":{"id":1234,"name":"raja"},"c":{"id":12345,"name":"rama"}}
ser = {1,2,44,556,66}
lst = [1,2,3]
lst.extend(dict["b"]["name"])
print(lst)


# operators
x,y,z= map(int,input().split())
if (x>y and x>z ):
    print("x is greater")
if (y>z and y>x ):
    print("y is greater")
else:
    print("z is greater")



# farenhit to kevin
def far_to_kel(n):
    res = (n-32) * 5/9 + 273.15
    print (f"{res:.2f}")

far_to_kel(n = float(input("Enter input: ")))




# While using tuple as key two variables are used in loop is to mention the values in the tuple
dict1 = {('apple',1):{"firut"},('tomoto',2):{"vege"}}
for x,y in dict1:
    print(y)
    for i in dict1.values():
        print(i)

res = 0
tup = ((1,2,3,4,5,6))
cus_ele = [1,2,3,4]


set2 = {1, True,0,False}
print(set2)


# uncommon elements in both str
S1 = 'aacdb'
S2 = 'gafd'
s1 = set(S1)
s2 = set(S2)
res = s1 ^ s2
list(res)
print("".join(res))


# Difference in two lists
list1 = [10, 15, 20, 25, 30, 35, 40]
list2 = [25, 40, 35] 
lst = []
for i in list1:
    if i not in list2:
        lst.append(i)
print(lst)


lst1 = set(list1)
lst2 = set(list2)
print(lst1-lst2)


# Check if frequency of all characters can become same by one removal
from collections import Counter
input = 'xxxyyzz'
dic = Counter(input)
res = list(set(dic.values()))
if len(res) > 2 :
    print("NO")
elif len(res)==2 and res[0] - res[1] > 1:
    print("No")
else:
    print("Yes")


# number between range
def in_range(a):
    if (a in range(r)):
        print("yes")
    else:
        print("No")
a = 2011
r = 50
in_range(a)

# Noof_upper_and_lower
def no_of_upper_and_lower(str1):
    upper = 0
    lower = 0
    for i in str1:
        if (i.isupper()):
            upper+=1
        else:
            lower+=1
    return upper,lower

str1 = 'The quick Brow Fox'
print(no_of_upper_and_lower (str1))

#Working of exec function
code = "print(\"raja\")"
exec(code)

# Sorting_String 
def sort_str(string):
    lst_str = (string.split("-"))
    lst_str.sort()
    return ("-".join(lst_str))
print(sort_str(string="green-red-yellow-black-white"))

# Is_panagram
def is_panagram(str_input):
    alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]
    str_input = str_input.lower()
    for i in alphabet:
        if i not in str_input:
            return False
    return True

print(is_panagram(str_input = "The quick brown fox jumps over the lazy dog"))

# * Args explaination
def avg(*arg):
    total = 0
    for i in arg:
        total += i
    return total//3

print(avg(1,2,3,4))


