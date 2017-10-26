# problem 1

s = 'azcbobobegghakl'
vowels = 'aeiou'
count = 0
for char in s:
    if char in vowels:
        count = count + 1
print('Number of vowels: ' + str(count))

# problem 2

s = 'azcbobobegghakl'
count = s.count('bob')
print('Number of times bob occurs is: ' + str(count) )

count = 0
start = 0
while True:
    start = s.find('bob', start) + 1
    if start > 0:
        count = count + 1
    else:
        break
print('Number of times bob occurs is: ' + str(count) )

# problem 3

s = 'zyxwvutsrqponmlkjihgfedcba'

# make true false list if in alpha-order
l = list()
for x in range(0,len(s)-1):    
    l.append( s[x] <= s[x+1] )

# make list with sequences 
l2 = list()
from itertools import groupby
from operator import itemgetter
for k,v in groupby(enumerate(l),key=itemgetter(1)):
    if k:
        v = list(v)
        a = v[0][0]
        b = v[-1][0]
        l2.append(s[a:b+2])

# if less than 1 in order, pick first letter
if not l2:
    q = s[0]
# return longest sequence
else:
    q = max(l2, key=len)

# print results
print('Longest substring in alphabetical order is: ' + q)