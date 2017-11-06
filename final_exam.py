#Problem 3 - Convert number to mandarin
def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    
    For numbers 11-19, the number is pronounced as "ten digit",
    so for example, 16 would be pronounced (using Mandarin) as "ten six".
    
    For numbers between 20 and 99, the number is pronounced as “digit ten digit”,
    so for example, 37 would be pronounced (using Mandarin) as "three ten seven".
    If the digit is a zero, it is not included.
    
    'trans' is a simple Python dictionary that captures the numbers between 0 and 10.
    '''
    trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}
    
    num = int(us_num)
    if num<=10:
        return trans[us_num]
    elif num>10 and num<20:
        return trans['10'] + ' ' + trans[str(num%10)]
    else:
        if num%10==0:
            return trans[str(num//10)] + ' ' + trans['10']
        else:
            return trans[str(num//10)] + ' ' + trans['10'] + ' ' + trans[str(num%10)]

print (convert_to_mandarin('36'))
print (convert_to_mandarin('20'))
print (convert_to_mandarin('16'))

#################################################################################

#Problem 4
def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    resultantL = []
    finalDecL = []
    finalIncL = []
    
    for i in range(len(L)-1):
        decL = []
        start = i
        decL.append(L[start])
        while L[start+1]<=L[start]:
            decL.append(L[start+1])
            if start+1==len(L)-1:
                break
            start += 1
        if len(decL)>len(finalDecL):
            finalDecL = decL
    
    for i in range(len(L)-1):
        incL = []
        start = i
        incL.append(L[start])
        while L[start+1]>=L[start]:
            incL.append(L[start+1])
            if start+1==len(L)-1:
                break
            start += 1
        if len(incL)>len(finalIncL):
            finalIncL = incL
    
    if len(finalDecL)>len(finalIncL):
        resultantL = finalDecL
    elif len(finalDecL)<len(finalIncL):
        resultantL = finalIncL
    else:
        if L.index(finalDecL[0]) < L.index(finalIncL[0]):
            resultantL = finalDecL
        else:
            resultantL = finalIncL
    
    print (finalDecL)
    print (finalIncL)
    print (resultantL)
    return sum(resultantL)

L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]
L1 = [5, 4, 10]
print (longest_run(L1))

#################################################################################

#Problem 5
"""
In this problem, you will implement a class according to the specifications in the template file-
usresident.py. The file contains a Person class similar to what you have seen in lecture and 
a USResident class (a subclass of Person). Person is already implemented for you and 
you will have to implement two methods of USResident.
## DO NOT MODIFY THE IMPLEMENTATION OF THE Person CLASS ##
"""

class Person(object):
    def __init__(self, name):
        #create a person with name name
        self.name = name
        try:
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank+1:]
        except:
            self.lastName = name
        self.age = None
    def getLastName(self):
        #return self's last name
        return self.lastName
    def setAge(self, age):
        #assumes age is an int greater than 0
        #sets self's age to age (in years)
        self.age = age
    def getAge(self):
        #assumes that self's age has been set
        #returns self's current age in years
        if self.age == None:
            raise ValueError
        return self.age
    def __lt__(self, other):
        #return True if self's name is lexicographically less
        #than other's name, and False otherwise
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    def __str__(self):
        #return self's name
        return self.name
        
class USResident(Person):
    """ 
    A Person who resides in the US.
    """
    def __init__(self, name, status):
        """ 
        Initializes a Person object. A USResident object inherits 
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """
        Person.__init__(self, name)
        self.status = status
        
    def getStatus(self):
        """
        Returns the status
        """
        if self.status!="citizen" and self.status!="legal_resident" and self.status!="illegal_resident":
            raise ValueError
        if self.status == "citizen":
            return self.status
        elif self.status == "legal_resident":
            return self.status
        elif self.status == "illegal_resident":
            return self.status
        
a = USResident('Tim Beaver', 'citizen')
print(a.getStatus())
b = USResident('Tim Horton', 'non-resident')

#################################################################################

#Problem 6.1
"""
Change the definition of ArrogantProfessor so that the following behavior is achieved:

e = Person('eric') 
le = Lecturer('eric') 
pe = Professor('eric') 
ae = ArrogantProfessor('eric')

>>> e.say('the sky is blue')
eric says: the sky is blue

>>> le.say('the sky is blue')
eric says: the sky is blue

>>> le.lecture('the sky is blue')
I believe that eric says: the sky is blue

>>> pe.say('the sky is blue')
eric says: I believe that eric says: the sky is blue

>>> pe.lecture('the sky is blue')
I believe that eric says: the sky is blue

>>> ae.say('the sky is blue')
eric says: It is obvious that eric says: the sky is blue

>>> ae.lecture('the sky is blue')
It is obvious that eric says: the sky is blue
"""

class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return self.name + ' says: It is obvious that ' + Person.say(self, stuff)
    def lecture(self, stuff): 
        return 'It is obvious that ' + Person.say(self, stuff)

e = Person('eric') 
le = Lecturer('eric') 
pe = Professor('eric') 
ae = ArrogantProfessor('eric')

print(e.say('the sky is blue'))
print(le.say('the sky is blue'))
print(le.lecture('the sky is blue'))
print(pe.say('the sky is blue'))
print(pe.lecture('the sky is blue'))
print(ae.say('the sky is blue'))
print(ae.lecture('the sky is blue'))

#################################################################################

#Problem 6.2
"""
Change the definition of ArrogantProfessor so that the following behavior is achieved:

>>> ae.say('the sky is blue')
eric says: It is obvious that I believe that eric says: the sky is blue

>>> ae.lecture('the sky is blue')
It is obvious that I believe that eric says: the sky is blue
"""
class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return self.name + ' says: It is obvious that ' + Lecturer.lecture(self, stuff)
    def lecture(self, stuff): 
        return 'It is obvious that ' + Lecturer.lecture(self, stuff)

e = Person('eric') 
le = Lecturer('eric') 
pe = Professor('eric') 
ae = ArrogantProfessor('eric')

print(e.say('the sky is blue'))
print(le.say('the sky is blue'))
print(le.lecture('the sky is blue'))
print(pe.say('the sky is blue'))
print(pe.lecture('the sky is blue'))
print(ae.say('the sky is blue'))
print(ae.lecture('the sky is blue'))

#################################################################################

#Problem 6.3
"""
Change the definition of Professor so that the following behavior is achieved:

>>> pe.say('the sky is blue')
Prof. eric says: I believe that eric says: the sky is blue 

>>> ae.say('the sky is blue')
Prof. eric says: It is obvious that I believe that eric says: the sky is blue 
"""
class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return 'Prof. ' + self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return self.name + ' says: It is obvious that ' + Lecturer.lecture(self, stuff)
    def lecture(self, stuff): 
        return 'It is obvious that ' + Lecturer.lecture(self, stuff)

e = Person('eric') 
le = Lecturer('eric') 
pe = Professor('eric') 
ae = ArrogantProfessor('eric')

print(e.say('the sky is blue'))
print(le.say('the sky is blue'))
print(le.lecture('the sky is blue'))
print(pe.say('the sky is blue'))
print(pe.lecture('the sky is blue'))
print(ae.say('the sky is blue'))
print(ae.lecture('the sky is blue'))

#################################################################################

#Problem 7
def general_poly(L):
    """ 
    L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0
    
    For example, general_poly([1, 2, 3, 4])(10) should evaluate to 1234 because 
    1*10^3 + 2*10^2 + 3*10^1 + 4*10^0
    """
    def value(x):
        total = 0
        k = len(L)-1
        for i in range(len(L)):
            total += L[i]*(x**k)
            k -= 1
        return total
    return value

L = [1, 2, 3, 4]
print (general_poly(L)(10))