# -*- coding: utf-8 -*-
"""
PROBLEM 1

Write a simple procedure, myLog(x, b), that computes the logarithm of a number x relative to a base b. 
For example, if x = 16 and b = 2, then the result is 4 - because 2^4=16. If x = 15 and b = 3, then the 
result is 2 - because 3^2 is the largest power of 3 less than 15.

In other words, myLog should return the largest power of b such that b to that power is still less 
than or equal to x.

x and b are both positive integers; b is an integer greater than or equal to 2. Your function should 
return an integer answer.

"""

def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    total = b
    count = 1
    while True:
        if total > x:
            count = count - 1
            break
        count = count + 1
        total = total * b
    return count 

"""
PROBLEM 2

Write a Python function that returns the sublist of strings in aList that contain fewer than 4 characters.
For example, if aList = ["apple", "cat", "dog", "banana"], your function should return: ["cat", "dog"]

This function takes in a list of strings and returns a list of strings. Your function should not modify 
aList.
"""

def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    newList = []
    for word in aList:
        if len(word) < 4:
            newList.append(word)
    return newList
            
"""
PROBLEM 3

Write a recursive Python function, given a non-negative integer N, to calculate and return the 
sum of its digits.

Hint: Mod (%) by 10 gives you the rightmost digit (126 % 10 is 6), while doing integer division 
by 10 removes the rightmost digit (126 / 10 is 12).

This function has to be recursive; you may not use loops!

This function takes in one integer and returns one integer.
"""

def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    if N < 10:
        return N
    return sumDigits(N/10) + N%10

"""
PROBLEM 4

Write a Python function that returns a list of keys in aDict with the value target. The list of keys you 
return should be sorted in increasing order. The keys and values in aDict are both integers. (If aDict does 
not contain the value target, you should return an empty list.)

This function takes in a dictionary and an integer and returns a list.
"""

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    newList = []    
    for x in aDict:
        if aDict[x] == target:
            newList.append(x)
    return newList

"""
PROBLEM 5

Write a Python function called satisfiesF that has the specification below. 
Then make the function call run_satisfiesF(L, satisfiesF). Your code should look like:

run_satisfiesF(L, satisfiesF)
For your own testing of satisfiesF, for example, the following test function f and test code:

def f(s):
    return 'a' in s
      
L = ['a', 'b', 'a']
print satisfiesF(L)
print L
Should print:

2
['a', 'a']

Paste your entire function satisfiesF, including the definition, in the box below. 
After you define your function, make a function call to run_satisfiesF(L, satisfiesF). 
Do not define f or run_satisfiesF. Do not leave any debugging print statements.

For this question, you will not be able to see the test cases we run. This problem will test 
your ability to come up with your own test cases.
"""

def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements
    Returns the length of L after mutation
    """
    result = []    
    for x in L:
        result.append( f(x) )
    for x in range(len(L)-1, -1 , -1):
        if result[x] == False:
            del L[x]
    return( len(L) )

def f(s):
    return 'a' in s
      
L = ['a', 'b', 'a']
print satisfiesF(L)
print L


