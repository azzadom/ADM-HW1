#################################
#Say "Hello, World!" With Python#
################################# 
my_string = "Hello, World!"
print(my_string)

################
#Python If-Else#
################
n = int(input().strip())

w = "Weird"
not_w = "Not Weird"

if (n%2) != 0:
    print(w)
else: 
    if 2 <= n <= 5: 
        print(not_w)
    elif 6 <= n <= 20: 
        print(w)
    elif n > 20: 
        print(not_w)

######################
#Arithmetic Operators#
######################
a = int(input())
b = int(input())

print(a+b)
print(a-b)
print(a*b)

##################
#Python: Division#
##################
a = int(input())
b = int(input())

print(a//b)
print(a/b)

#######
#Loops#
#######
n = int(input())
for i in range(0,n):
    print(i**2)

##################
#Write a function#
##################
def is_leap(year):
    leap = False

    if (year%4) == 0:
        if (year%100) == 0:
            if(year%400) == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else: 
        leap = False

    return leap

year = int(input())
print(is_leap(year))

################
#Print Function#
################
n = int(input())

for i in range(1, n+1): 
    print(i, end="")

#####################
#List Comprehensions#
#####################
x = int(input())
y = int(input())
z = int(input())
n = int(input())

#Use a lambda function to create a list of all possible coordinates given the values of x, y, z, and n
l = [[i, j, k] 
    for i in range(x + 1)  
    for j in range(y + 1)  
    for k in range(z + 1)  
    if i + j + k != n]     

print(l)

###########################
#Find the Runner-Up Score!#
###########################
n = int(input())
arr = map(int, input().split())

lst = list(arr)
lst.sort(reverse=True)
print(lst[lst.count(lst[0])])

##############
#Nested Lists#
##############
students = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name,score])

grades = [grade for name, grade in students]
grades.sort()
sec_low_grade = grades[grades.count(grades[0])]
sec_low_studs = [name for name, grade in students if grade == sec_low_grade]
sec_low_studs.sort()

print("\n".join(sec_low_studs))

########################
#Finding the percentage#
########################
n = int(input())

student_marks = {}

for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input()
marks = student_marks.get(query_name)
print("{:.2f}".format(sum(marks)/3))

#######
#Lists#
#######
N = int(input())

lst = []

for _ in range(N):
    command = input().split()
    
    if command[0] == "insert":
        lst.insert(int(command[1]),int(command[2]))
    elif command[0] == "print":
        print(lst)
    elif command[0] == "remove":
        lst.remove(int(command[1]))
    elif command[0] == "append":
        lst.append(int(command[1]))
    elif command[0] == "sort":
        lst.sort()
    elif command[0] == "pop":
        lst.pop()
    elif command[0] == "reverse":
        lst.reverse()

########            
#Tuples#
########
n = int(input())
integer_list = map(int, input().split())

t = tuple(integer_list)
print(hash(t))

###########
#sWAP cASE#
###########
def swap_case(s):
    return s.swapcase()

s = input()
result = swap_case(s)
print(result)

#######################
#String Split and Join#
#######################
def split_and_join(line):
    return "-".join(line.split(" "))

line = input()
result = split_and_join(line)
print(result)

##################
#What's Your Name#
##################
def print_full_name(first, last):
    generic = "Hello firstname lastname! You just delved into python."
    output = generic.replace("firstname", first).replace("lastname", last)
    print(output)

first_name = input()
last_name = input()
print_full_name(first_name, last_name)

###########
#Mutations#
###########
def mutate_string(string, position, character):
    return string[:position] + character + string[(position+1):]

s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)

###############
#Find a string#
###############
def count_substring(string, sub_string):  
    pos = 0
    count = 0

    l = len(string)

    while 0 <= pos < l:
        pos = string.find(sub_string, pos, l)
        if pos != -1:
            pos += 1
            count += 1
        
    return count

string = input().strip()
sub_string = input().strip()

count = count_substring(string, sub_string)
print(count)

###################
#String Validators#
###################
s = input()
alnum = False
alpha = False
digit = False
lower = False
upper = False

for i in s:
    if (i.isalnum()):
        alnum = True
    if (i.isalpha()):
        alpha = True
    if (i.isdigit()):
        digit = True
    if (i.islower()):
        lower = True
    if (i.isupper()):
        upper = True

print (alnum)
print (alpha)
print (digit)
print (lower)
print (upper) 

################
#Text Alignment#
################
thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

###########
#Text Wrap#
###########
import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)

###################
#Designer Door Mat#
###################
inputs = list(map(int, input().split()))
n = inputs[0]
m = inputs[1]
center_line = n//2 + 1
s = ".|."

for i in range(0, center_line - 1):
    print (((s*i)+s+(s*i)).center(m,'-'))

print ("WELCOME".center(m,'-'))

for i in range(center_line, n):
    k = n - i - 1
    print (((s*k)+s+(s*k)).center(m,'-'))

###################
#String Formatting#
###################
def print_formatted(number):
    
    # -2 to ignore '0b' prefix
    width = len(bin(number)) - 2  
    
    for i in range(1, number + 1):
        # Print each format, ensuring right alignment
        decimal = str(i).rjust(width)
        octal = oct(i)[2:].rjust(width)  # Remove '0o' prefix
        hexadecimal = hex(i)[2:].upper().rjust(width)  # Remove '0x' prefix and capitalize
        binary = bin(i)[2:].rjust(width)  # Remove '0b' prefix

        print(f"{decimal} {octal} {hexadecimal} {binary}")

n = int(input())
print_formatted(n)

##################
#Alphabet Rangoli#
##################
def print_rangoli(size):
    max_w = (2*size - 1)*2 - 1

    alpha = list(map(chr, range(ord('a'), ord('z')+1)))
    lines_up = []
    lines_down = []

    for i in range(0, size-1):    

        s = "-".join(alpha[size-1:size-i-2:-1] + alpha[size-i:size])

        lines_up.append(s.center(max_w, '-'))

        lines_down.append(s.center(max_w, '-'))

    complete_line = "-".join(alpha[size-1::-1] + alpha[1:size])
    lines_up.append(complete_line)
    lines_down.reverse()

    print ( "\n".join(lines_up + lines_down))

n = int(input())
print_rangoli(n)

#############
#Capitalize!#
#############
def solve(s):
    l = s.split(" ")

    for i in range(len(l)):
        l[i] = l[i].capitalize()

    return ' '.join(l)

fptr = open(os.environ['OUTPUT_PATH'], 'w')
s = input()
result = solve(s)
fptr.write(result + '\n')
fptr.close()

#################
#The Minion Game#
#################
def minion_game(string):
    l = len(string)
    k_points = 0  
    s_points = 0  

    for i in range(l):
        # Points are determined by how many substrings start from index i
        if string[i] in "AEIOU":
            k_points += l - i  # All substrings starting with this vowel
        else:
            s_points += l - i  # All substrings starting with this consonant

    if k_points > s_points:
        print("Kevin", k_points)
    elif s_points > k_points:
        print("Stuart", s_points)
    else:
        print("Draw")

s = input()
minion_game(s)

##################
#Merge the Tools!#
##################
def merge_the_tools(string, k):
    n = len(string)
    sub_num = n//k
    
    sub_strings_rep = []

    for i in range(sub_num):
        sub_strings_rep.append(string[i*k:(i+1)*k])
    
    for i in sub_strings_rep:
        sub_final = ""
        for j in i:
            if j not in sub_final:
                sub_final += j
        print(sub_final)    

string, k = input(), int(input())
merge_the_tools(string, k)

######################
#Introduction to Sets#
######################
def average(array):
    s = set(array)
    return round(sum(s)/len(s), 3)

n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)

######################
#Symmetric Difference#
######################
m = int(input())
m_set = set(map(int, input().split()))
n = int(input())
n_set = set(map(int, input().split()))

sym_list = list(n_set.symmetric_difference(m_set))
sym_list.sort()

for i in sym_list:
    print(i)

##########
#No Idea!#
##########
line = list(map(int, input().split()))
n, m = line[0], line[1]
array = list(map(int, input().split()))
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

happiness = 0

for i in array:
    if i in set_a:
        happiness += 1
    elif i in set_b:
        happiness -= 1

print(happiness)

############
#Set .add()#
############
n = int(input())
country_set = set()
for _ in range(n):
    s = input()
    country_set.add(s)

print(len(country_set))

####################################
#Set .discard(), .remove() & .pop()#
####################################
n = int(input())
s = set(map(int, input().split()))

m = int(input())

for _ in range(m):
    command = input().split()
    
    if command[0] == "pop":
        s.pop()
    elif command[0] == "remove":
        s.remove(int(command[1]))
    elif command[0] == "discard":
        s.discard(int(command[1]))

print(sum(s))

########################
#Set .union() Operation#
########################
n_eng = int(input())
s_eng = set(map(int, input().split()))
n_fr = int(input())
s_fr = set(map(int, input().split()))

print(len(s_fr.union(s_eng)))

###############################
#Set .intersection() Operation#
###############################
n_eng = int(input())
s_eng = set(map(int, input().split()))
n_fr = int(input())
s_fr = set(map(int, input().split()))

print(len(s_fr.intersection(s_eng)))

#############################
#Set .difference() Operation#
#############################
n_eng = int(input())
s_eng = set(map(int, input().split()))
n_fr = int(input())
s_fr = set(map(int, input().split()))

print(len(s_eng.difference(s_fr)))

#######################################
#Set .symmetric_difference() Operation#
#######################################
n_eng = int(input())
s_eng = set(map(int, input().split()))
n_fr = int(input())
s_fr = set(map(int, input().split()))

print(len(s_eng.symmetric_difference(s_fr)))

###############
#Set Mutations#
###############
n = int(input())
s = set(map(int, input().split()))

m = int(input())

for _ in range(m):
    command = input().split()
    
    if command[0] == "intersection_update":
        s_new = set(map(int, input().split()))
        s.intersection_update(s_new)
    elif command[0] == "update":
        s_new = set(map(int, input().split()))
        s.update(s_new)
    elif command[0] == "symmetric_difference_update":
        s_new = set(map(int, input().split()))
        s.symmetric_difference_update(s_new)
    elif command[0] == "difference_update":
        s_new = set(map(int, input().split()))
        s.difference_update(s_new)
        
print(sum(s))

####################
#The Captain's Room#
####################
k = int(input())

room_list = list(map(int, input().split()))
room_set = set(room_list)

# list_sum is the sum of all the rooms in the room_list, where each family's rooms are repeated k times plus the captain's room
list_sum = sum(room_list)

# set_sum is the sum of all unique rooms in the room_set, multiplied by k
set_sum = sum(room_set) * k

# By subtracting list_sum from set_sum, we get the captain's room multiplied by (k-1)
# Dividing by (k-1) gives us the captain's room
captain_room = (set_sum - list_sum) // (k-1)
    
print(captain_room)

##############
#Check Subset#
##############
t = int(input())

for _ in range(t):
    n_a = int(input())
    set_a = set(map(int, input().split()))
    n_b = int(input())
    set_b = set(map(int, input().split()))
    
    set_u = set_b.union(set_a)
    
    print(set_u == set_b)

#######################
#Check Strict Superset#
#######################
set_a = set(map(int, input().split()))
n = int(input())

strict_superset = True

for _ in range(n):
    set_b = set(map(int, input().split()))
    if not set_a.issuperset(set_b):
        strict_superset = False
        break

print(strict_superset)

#######################
#Collections.Counter()#
#######################
from collections import Counter

n = int(input())
shoe_sizes = list(map(int, input().split()))
count_sizes = Counter(shoe_sizes)

cust = int(input())
money = 0

for _ in range(cust):
    size, price = map(int, input().split())
    if count_sizes[size] > 0:
        money += price
        count_sizes[size] -= 1


print(money)

######################
#DefaultDict Tutorial#
######################
from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(list)

#Add the index to the list associated with the character key
for i in range(n):
    d[input()].append(i+1)

#Print the list of indices for each character key
for i in range(m):
    k = input()
    if k in d:
        print(" ".join(map(str, d[k])))
    else:
        print(-1)

##########################
#Collections.namedtuple()#
##########################
from collections import namedtuple

students = []
n = int(input())

Student = namedtuple('Student', input())

for _ in range(n):
    s = input().split()
    students.append(Student(s[0], s[1], s[2], s[3]))

print(sum([int(s.MARKS) for s in students])/n)

###########################
#Collections.OrderedDict()#
###########################
from collections import OrderedDict

items = OrderedDict()
n = int(input())

for _ in range(n):
    line = input().split()
    name = " ".join(line[:len(line)-1])
    price = int(line[len(line)-1])
        
    if name in items:
        items[name] += price
    else:
        items[name] = price

for i in items:
    print(i,items.get(i)) 

############
#Word Order#
############
from collections import Counter
from collections import OrderedDict

n = int(input())

l = []
for _ in range(n):
    l.append(input())

d = OrderedDict(Counter(l))
print(len(d))
print(*d.values())

#####################
#Collections.deque()#
#####################
from collections import deque

d = deque()
n = int(input())

for _ in range(n):
    command = input().split()
    
    if command[0] == "append":
        d.append(int(command[1]))
    elif command[0] == "appendleft":
        d.appendleft(int(command[1]))
    elif command[0] == "pop":
        d.pop()
    elif command[0] == "popleft":
        d.popleft()

print(*d)

##############
#Company Logo#
##############
from collections import Counter
from collections import OrderedDict

s = input()
d = OrderedDict(Counter(s))

d_sort = sorted(d.items(), key=lambda x: (-x[1], x[0]))

for i in range(3):
    print(d_sort[i][0], d_sort[i][1])
    
############
#Piling Up!#
############
from collections import deque
t = int(input())

for _ in range(t):
    n = int(input())
    cubes = deque(map(int, input().split()))

    result = "Yes"
    
    if cubes[0] >= cubes[-1]:
        base = cubes.popleft()
    else:
        base = cubes.pop()
    
    while cubes:
        if cubes[0] >= cubes[-1] and cubes[0] <= base:
            base = cubes.popleft()
        elif cubes[-1] <= base:
            base = cubes.pop()
        else:
            result = "No"
            break
    
    print(result)

#################
#Calendar Module#
#################
import calendar

date = list(map(int, input().split()))

day = calendar.weekday(date[2], date[0], date[1])

days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

print(days[day])

############
#Time Delta#
############
from datetime import datetime

def time_delta(t1, t2):
    string_format = '%a %d %b %Y %H:%M:%S %z'
    dt1 = datetime.strptime(t1, string_format) 
    dt2 = datetime.strptime(t2, string_format)

    return str(abs(int((dt1 - dt2).total_seconds())))

############
#Exceptions#
############
n = int(input())

for _ in range(n):
    a, b = input().split()
    try:
        print(int(a)//int(b))
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)

#########
#Zipped!#
#########
students, subjects = input().split()

students = int(students)
subjects = int(subjects)

scores = [] 

for _ in range(subjects):
    scores += [list(map(float, input().split()))]

scores_tot = zip(*scores)

for student_scores in scores_tot:
    print(sum(student_scores)/subjects)

##############
#Athlete Sort#
##############
nm = input().split()
n = int(nm[0])
m = int(nm[1])
arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

k = int(input())

arr.sort(key=lambda x: x[k])

for i in arr:
    print(*i)

#########
#ginortS#
#########
s = input()

lower = []
upper = []
odd = []
even = []

for i in s:
    if i.islower():
        lower.append(i)
    elif i.isupper():
        upper.append(i)
    elif i.isdigit():
        if int(i)%2 == 0:
            even.append(i)
        else:
            odd.append(i)

lower.sort()
upper.sort()
odd.sort()
even.sort()

print("".join(lower + upper + odd + even))

#########################
#Map and Lambda Function#
#########################
cube = lambda x: x**3

def fibonacci(n):
    f = [0, 1]
    for i in range(2, n):
        f.append(f[i-1] + f[i-2])
    return f[:n]

##############################
#Detect Floating Point Number#
##############################
import re

n = int(input())
inputs = [input() for _ in range(n)]

pattern = re.compile(r"^[+-]?\d*\.\d+$")

for i in inputs:
    print(bool(pattern.match(i)))

############
#Re.split()#
############
regex_pattern = r"\,|\."	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))

#################################
#Group(), Groups() & Groupdict()#
#################################
import re

#the \1 refers to the first capturing group of ([a-zA-Z0-9]), and the + quantifier means "one or more times."
m = re.search(r"([a-zA-Z0-9])\1+", input()) 

if m:
    print(m.group(0))
else:
    print(-1)

################
#Re.findall() & Re.finditer()#
################
import re

pattern = r"(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])"

sub = re.findall(pattern, input())

if sub:
    for i in sub:
        print(i)
else:
    print(-1)

#######################
#Re.start() & Re.end()#
#######################
import re

s = input()
k = input()
start = 0

index = []

while start < len(s):
    m = re.search(k, s[start:])
    if m:
        index.append((m.start() + start, m.end() + start - 1))
        start += m.start() + 1
    else:
        break

if index:
    for i in index:
        print(i)
else:
    print((-1,-1))

####################
#Regex Substitution#
####################
import re
n = int(input())

for _ in range(n):
    s = input()
    s = re.sub(r"(?<= )(&&)(?= )", "and", s)
    s = re.sub(r"(?<= )(\|\|)(?= )", "or", s)
    print(s)

###########################
#Validating Roman Numerals#
###########################
regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

import re
print(str(bool(re.match(regex_pattern, input()))))

##########################
#Validating phone numbers#
##########################
import re

regex_pattern = r"^[789]\d{9}$"

n = int(input())

for _ in range(n):
    if re.match(regex_pattern, input()):
        print("YES")
    else:
        print("NO")

########################################
#Validating and Parsing Email Addresses#
########################################
import re
import email.utils

n = int(input())

for _ in range(n):
    s = input()
    data = email.utils.parseaddr(s)
    e = data[1]
    if re.match(r'^[a-zA-Z][\w\.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$', e):
        print(s)

#######################
#Hex Color Code#
#######################
import re

n = int(input())

for _ in range(n):
    s = input()
    for i in re.findall(r'(\#[a-fA-F0-9]{3,6})[\;\,\)]{1}', s):
        print(i)
    
######################
#HTML Parser - Part 1#
######################
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for i in attrs:
            print("->", i[0], ">", i[1])

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for i in attrs:
            print("->", i[0], ">", i[1])

n = int(input())

parser = MyHTMLParser()

for _ in range(n):
    parser.feed(input())

######################
#HTML Parser - Part 2#
######################
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if "\n" in data:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)

    def handle_data(self, data):
        if data != "\n":
            print(">>> Data")
            print(data)    
   
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()

###################################################
#Detect HTML Tags, Attributes and Attribute Values#
###################################################
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for i in attrs:
            print("->", i[0], ">", i[1])

    def handle_startendtag(self, tag, attrs):
        print(tag)
        for i in attrs:
            print("->", i[0], ">", i[1])

html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()

################
#Validating UID#
################
import re

regex = r"^(?!.*(.).*\1)(?=(?:.*[A-Z]){2,})(?=(?:.*\d){3,})[a-zA-Z0-9]{10}$"

n = int(input())

for _ in range(n):
    s = input()
    if re.match(regex, s):
        print("Valid")
    else:
        print("Invalid")

################################
#Validating Credit Card Numbers#
################################
import re

n = int(input())

for _ in range(n):
    s = input()
    if re.match(r"^[456]\d{3}(-?\d{4}){3}$", s) and not re.search(r"(\d)\1{3,}", s.replace("-", "")):
        print("Valid")
    else:
        print("Invalid")

#########################
#Validating Postal Codes#
#########################
regex_integer_in_range = r"^[1-9][\d]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	# Do not delete 'r'.


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

###############
#Matrix Script#
###############
#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

matrix = list(zip(*matrix))

s = ""

for i in matrix:
    s += "".join(i)

#Replace non-alphanumeric characters with spaces in between alphanumeric characters
print(re.sub(r"(?<=\w)([^\w\d]+)(?=\w)", " ", s)) 

########################
#XML 1 - Find the Score#
########################
import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    attr_num = 0
    for i in node.iter():
        attr_num += len(i.attrib)
    return attr_num
        

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))

###############################
#XML2 - Find the Maximum Depth#
###############################
import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    level += 1
    if level >= maxdepth:
        maxdepth = level
    for i in elem:
        depth(i, level)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)

############################################
#Standardize Mobile Number Using Decorators#
############################################
def wrapper(f):
    def fun(l):
        f(["+91 "+n[-10:-5]+" "+n[-5:] for n in l])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 

###############################
#Decorators 2 - Name Directory#
###############################
import operator

def person_lister(f):
    def inner(people):
        for i in people:
            people[2] = int(people[2])
        people.sort(key=operator.itemgetter(2))
        return [f(p) for p in people]
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

########
#Arrays#
########
import numpy

def arrays(arr):
    a = numpy.array(arr, dtype=float)
    return a[::-1] 

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

###################
#Shape and Reshape#
###################
import numpy

arr = numpy.array(list(map(int, input().split())))
print (numpy.reshape(arr, (3,3)))

#######################
#Transpose and Flatten#
#######################
import numpy

inputs = list(map(int, input().split()))
n = inputs[0]
m = inputs[1]

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

arr = numpy.array(arr)

print(numpy.transpose(arr))
print(arr.flatten())

#############
#Concatenate#
#############
import numpy

inputs = list(map(int, input().split()))
n = inputs[0]
m = inputs[1]
p = inputs[2]

arr_n = []
arr_m = []

for _ in range(n):
    arr_n.append(list(map(int, input().split())))
    
for _ in range(m):
    arr_m.append(list(map(int, input().split())))

arr_n = numpy.array(arr_n)
arr_m = numpy.array(arr_m)

print(numpy.concatenate((arr_n,arr_m)))

################
#Zeros and Ones#
################
import numpy

shape = tuple(map(int, input().split()))

print(numpy.zeros(shape, dtype = int))
print(numpy.ones(shape, dtype = int))

##################
#Eye and Identity#
##################
import numpy
numpy.set_printoptions(legacy='1.13')

n, m = map(int, input().split())

print (numpy.eye(n, m, k = 0))

###################
#Array Mathematics#
###################
import numpy

n, m = map(int, input().split())

a = []
b = []

for _ in range(n):
    a.append(list(map(int, input().split())))

for _ in range(n):
    b.append(list(map(int, input().split())))

a = numpy.array(a)
b = numpy.array(b)

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(a**b)

######################
#Floor, Ceil and Rint#
######################
import numpy
numpy.set_printoptions(legacy='1.13')


arr = numpy.array(list(map(float, input().split())))

print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))

##############
#Sum and Prod#
##############
import numpy

n, m = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

arr = numpy.array(arr)

print(numpy.prod(numpy.sum(arr, axis = 0)))

#############
#Min and Max#
#############
import numpy

n, m = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

arr = numpy.array(arr)

print(numpy.max(numpy.min(arr, axis = 1)))

####################
#Mean, Var, and Std#
####################
import numpy

n, m = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

arr = numpy.array(arr)

print(numpy.mean(arr, axis = 1))
print(numpy.var(arr, axis = 0))
print(round(numpy.std(arr), 11))

###############
#Dot and Cross#
###############
import numpy

n = int(input())

a = []
b = []

for _ in range(n):
    a.append(list(map(int, input().split())))
    
for _ in range(n):
    b.append(list(map(int, input().split())))
    
a = numpy.array(a)
b = numpy.array(b)

result = []

for j in range(n):
    row = []
    for i in range(n):
        row.append(numpy.dot(a[j],b[:,i]))
    result.append(row)

result = numpy.array(result)

print(result)
        
#################
#Inner and Outer#
#################
import numpy

a = numpy.array(list(map(int, input().split())))
b = numpy.array(list(map(int, input().split())))

print(numpy.inner(a,b))
print(numpy.outer(a,b))

#############
#Polynomials#
#############
import numpy

p = list(map(float, input().split()))
x = float(input())

print(numpy.polyval(p, x))

################
#Linear Algebra#
################
import numpy

n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(float, input().split())))

arr = numpy.array(arr, dtype = float)
    
print(round(numpy.linalg.det(arr), 2))

#######################
#Birthday Cake Candles#
#######################
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    max_h = max(candles)
    return candles.count(max_h)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

###################
#Number Line Jumps#
###################
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    if x2>x1 and v2>v1:
        return "NO"
    if abs(v2-v1)!=0 and (abs(x2-x1) % abs(v2-v1))==0:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

###################
#Viral Advertising#
###################
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    like = 0
    shared = 5
    for _ in range(n):
        like += shared//2
        shared = (shared//2)*3
    return like
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

#####################
#Recursive Digit Sum#
#####################
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    l = map(int, list(n))
    p = str(sum(l) * k)
    while (len(p)>1):
        l = map(int, list(p))
        p = str(sum(l))
    return int(p)
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

##################
#Insertion Sort 1#
##################
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    for i in range(n):
        v = arr[i]
        j = i-1
        while(j>=0 and arr[j]>v):
            arr[j+1] = arr[j]
            j = j-1
            print(*arr)
        arr[j+1] = v
    print(*arr)



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

##################
#Insertion Sort 2#
##################
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    for i in range(1,n):
        v = arr[i]
        j = i-1
        while(j>=0 and arr[j]>v):
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = v
        print(*arr)


        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
