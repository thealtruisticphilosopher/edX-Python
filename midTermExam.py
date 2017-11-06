#Problem 4
'''
base: base of the exponential, integer > 1
num: number you want to be closest to, integer > 0
Find the integer exponent such that base**exponent is closest to num.
Note that the base**exponent may be either greater or smaller than num.
In case of a tie, return the smaller value.
Returns the exponent.
'''
def closest_power(base, num):
    exp = 1
    res = base**exp
    while res<num:
        exp += 1
        res = base**exp
    diff1 = abs(num-base**(exp-1))
    diff2 = abs(num-res)
    
    if diff1<=diff2:
        return exp-1
    else:
        return exp

print (closest_power(3,12))
print (closest_power(4,12))       
print (closest_power(4,100))
        

#Problem 5
'''
Write a Python function that returns the sum of the pairwise products of listA and listB.
You should assume that listA and listB have the same length and are two lists of integer numbers.
For example, if listA = [1, 2, 3] and listB = [4, 5, 6], the dot product is 1*4 + 2*5 + 3*6,
meaning your function should return: 32
'''
def dotProduct(listA, listB):
    sum = 0
    for i in range(len(listA)):
        prod = listA[i] * listB[i]
        sum += prod
    return sum

listA = [1, 2, 3]
listB = [4, 5, 6]
print (dotProduct(listA, listB))


#Problem 6
""" assumes L is a list of lists whose elements are ints
Mutates L such that it reverses its elements and also 
reverses the order of the int elements in every element of L. 
It does not return anything.
"""
def deep_reverse(L):
    L.reverse()
    for i in range(len(L)):
        L[i].reverse()
    return L

L = [[1, 2], [3, 4], [5, 6, 7]]
print (deep_reverse(L))


#Problem 7
"""
Assume you are given two dictionaries d1 and d2, each with integer keys and integer values.
You are also given a function f, that takes in two integers, performs an unknown operation on them,
and returns a value.
Write a function called dict_interdiff that takes in two dictionaries (d1 and d2).
The function will return a tuple of two dictionaries: a dictionary of the intersect of d1 and d2,
and a dictionary of the difference of d1 and d2.
"""
def f(a,b):
    return a>b

def dict_interdiff(d1, d2):
    dicl = {}
    dics = {}
    dicsum = {}
    dicdiff = {}
    tup = ()
    if len(d1)>=len(d2):
        dicl = d1
        dics = d2
    else:
        dicl = d2
        dics = d1
    for i in dicl.keys():
        if i in dics.keys():
            dicsum.update({i:f(d1.get(i, 0), d2.get(i, 0))})
        else:
            dicdiff.update({i:dicl.get(i, 0)})
    for i in dics.keys():
        if i not in dicl.keys():
            dicdiff.update({i:dics.get(i, 0)})
    tup = (dicsum, dicdiff)        
    return tup

d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
d3 = {1:30, 2:20, 3:30}
d4 = {1:40, 2:50, 3:60}
d5 = {1: 1, 2: 2, 3: 3, 4: 4}
d6 = {1: 1, 2: 2, 3: 3, 4: 5, 6: 2}
print (dict_interdiff(d3, d4))


#Problm 8
"""
Assumes L is a list of integers
Assume functions f1 and g are defined for you. 
f1 takes in an integer, applies a function, returns another integer 
g takes in an integer, applies a Boolean function, returns either True or False
Mutates L such that, for each element i originally in L, L contains i if g(f1(i)) returns True,
and no other elements
Returns the largest element in the mutated L or -1 if the list is empty
"""
def f1(i):
    return i+2

def g(i):
    return i>5
    
def applyF_filterG(L, f1, g):
    i = 0
    while i<len(L):
        if not (g(f1(L[i]))):
            del L[i]
        else:
            i = i+1
    
    if len(L)==0:
        return -1
    elif len(L)==1:
        return L[0]
    else:
        return max(L)

L = [0, -10, 5, 6, -4]
print(applyF_filterG(L, f1, g))
print(L)


#Problem 9
"""
Write a function to flatten a list.
The list contains other lists, strings, or ints.
For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened into
[1,'a','cat',2,3,'dog',4,5] (order matters).
"""
def flatten(aList):
    flat = []
    for i in aList:
        if type(i)==type(aList):
            flat.extend(flatten(i))
        else:
            flat.append(i)
    return flat

aList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
bList = [[1, [2, 3]], [[4, 5, 6], [7, [8, 9]]], [[3, 2, 1], [2, 1], [1, [0]]]]
print (flatten(aList))