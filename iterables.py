# module 1 exercise: iterables
import collections

###########################################
# 0. string review
# create a list with the strings: 'ab', 'cd'... 'mn'
# print data in the list, with all data on one line

#myList = ["ab", "cd", "ef", "gh", "ij", "kl", "mn"]
myList = "ab cd ef gh ij kl mn".split()

print(myList)
print(' '.join(myList)) #Prints without the formatting 

###########################################

# 1. named tuple 
# what does the following code do?
#sales = []
#sales.append((123, "pen", 20, 3))  #sales is a list of tupples 
#sales.append((456, "keyboard", 14, 30))
#print(sales[0][-1]) # print 3

# change sales to use named tuples 
Sale = collections.namedtuple("Sale", "id name quantity price")
sales = [ ]      # create a list of 
sales.append(Sale(145, "pen", 25, 6.35))
sales.append(Sale(832, "keyboard", 12, 23.95))
print(sales[0][-1])              # using indexing, print 6.35

#print(sales[0][-1])
# use field name to print the name and quantity of each product
for item in sales :
     print(item.name, item.quantity)

     

###########################################
# 2. default dictionary
# use a default dictionary to count the number of unique
# characters in a string, then print the character and the count.
mystr = "python programming"

myDefaultDict = collections.defaultdict(int)
for char in mystr :
     myDefaultDict[char] += 1
#print(myDefaultDict)
for char in sorted(myDefaultDict):
     print(char, myDefaultDict[char])
     
     

'''
###########################################
# 3. pack and unpack
L = [1, 2, 3, 4, 5, 6, 7]
# write code to store L[0] into the variable "first", 
# L[1] into the variable "second", and the rest of the L
# into the list called "rest"
first = L[0]
second = L[1]

rest = L[2:]
(first, second, *rest) = L   #packs the rest of list into rest 
print(first, second, rest)

#print(first, second, rest)


L = (1, 2, 3)
def f(a, b, c) :
    print(a, b, c)
    
f(*L) #unpacking! 
f( *L[:3]) # this allwos us to specifiy which we pass into the f function 
f(10, *L[1:3]) # this allwos us to specifiy which we pass into the f function 


# write code to call function f and pass to it the
# 3 values of L



###########################################
# 4. any, all
list1 = [10,20,30,40,-50]
print("any:", end=" ")
# write code to checck if any value in list1 is negative
# and print True, otherwise print False
print(any(item < 0 for item in list1))

print("all:", end=" ")
# write code to check if all values in list1 are positive
# and print True, otherwise print False

print(all(item > 0 for item in list1))



###########################################
# 5. enumerate
# what does the following code print?
list1 = [10,20,30,40,-50]
for i,item in enumerate(list1, start=3) :
    print(i, item)
# 3 10
# 4 20
# 5 30 
#etc

dict1 = {1:"one", 2:"two", 3:"three"}
for k,v in dict1.items() :
    print(k, v)



###########################################

# 6. len, min, max, reversed, ordered, sum
# what value the following code print?
tuple1 = (3, -2, 1, 9, 4, -3, 0)
print("len = ", len(tuple1)) #7
print("min = ", min(tuple1)) #-3
print("max = ", max(tuple1)) #9

# explain what is printed here:
print("reversed = ")
print(reversed(tuple1)) #DOES NOT prints elements in reversed order. 0, -3, 4, .... it returns an itorator object 
print(list(reversed(tuple1))) #this will work ! Has to explicitly request the data 

# fill in the empty string with an explanation for what's being printed


print(" ", sorted(tuple1)) # prints elements in ascending sorted order  

print(" ", sum(tuple1))
print(" ", sum(tuple1, 1000))




###########################################
# 7. zip
# what does the following code print?
#list1 -- 0,1,2,3,4
#list2 -- 10, 11, 12, 13, 14
#list3 -- 0 - 3
#shortest list dictates how many tuples you end up with 
for t in zip(range(5), range(10,15), range(4)) :
    print(t)
print()

#keys 0-4
#values 10-14
dict1 = dict(zip(range(5), range(10,15)))
for k,v in dict1.items() :
    print(k, v)
print()





###########################################
# 8. copy
# a. immutable objects
str1 = "hello"
str2 = str1
del(str1)
print(str2)    # will this be an error? no
#print(str1)   # will this be an error? yes 
#immutable objects can be copied this way 




# b. mutable objects
list1 = [1,2,3]
list2 = list1  #cannot be copied. simply creates a reference 
print(list2 is list1)  #prints true 
list1.pop()
print(list2)    # what's printed? [1,2]

list2 = list(list1)  #this is the way to copy mutable objects  
print(list2 is list1)  #prints flase since they are 2 differnt objects 
list1.append(10) 
print(list2)    # what's printed? origional list 2. it did not change 
print()




# c. data structures
dict1 = {"ones":[1,2,3], "tens":[10,20,30], "hundred":[100,200,300]}
dict2 = dict(dict1)
print("dict2:", end=" ")
for k,v in dict2.items() : print(k,v)
dict1["hundred"][-1] = 'a'            # change dict1
print("dict2:", end=" ")
for k,v in dict2.items() : print(k,v)    # is dict2 changed?




# this goes for list of lists, dictionary of tuples, etc.

list1 = [ [num for num in range(3)] for row in range(4) ]
print("list1:", end=" ")    # what's printed?
print(list1)

# write code to manually deep copy list1 into list2
list2 = [ ]
for row in list1:
    list2.append(list(row)) #otherwise it would make a reference to row. now we make a new list 
    
#this is non-nested comprehension     
list2 = [list(row) for row in list1]


list1[-1][-1] = 'ZZ'     # change list1
print("list2:", end=" ")
for elem in list2 :
    print(elem)          # list2 doesn't change
print()
# or using deepcopy of copy module


import copy
list2 = copy.deepcopy(list1)

list1[-1][-1] = 'A'
print("list2:", end=" ")
for elem in list2 :
    print(elem)    
print()



###########################################
# 9. iterator and generator
# a. Explain the code of this iterator
class Fib : 
    def __init__(self): 
        self._prev = 0  #inits the first 2 #'s in the fib sequence. adds previous one to the current 
        self._curr = 1                       
    def __iter__(self):        
        return self
    def __next__(self):       
        value = self._curr    
        self._curr += self._prev       
        self._prev = value
        return value	
 
 
 

# add code to keep printing a fibonacci number until the user chooses to end   

myfib = Fib()

answer = input("Enter key for next fibonacci number, or any character to end: ")
while answer == "" :
    print(next(myfib))
    answer = input("Enter key for next fibonacci number, or any character to end: ")
print()

# b. Explain the code of this generator
def FibGen() : #generator is created by a fucntion.  
    (prev, curr) = (0, 1)
    while True :
        yield curr  #keyword yield to create next value in sequence 
        prev, curr = curr, curr + prev
        
myfib = FibGen()
answer = input("Enter key for next fibonacci number, or any character to end: ")
while answer == "" :
    print(next(myfib))
    answer = input("Enter key for next fibonacci number, or any character to end: ")
print()
  
   
# on your own: copy the code above to let the user keep printing fibonacci numbers
# write a generator to let the user print the next squared value

def squareGen() : #generator is created by a function.  
    i = 1
    while True :
        yield i * i  #keyword yield to create next value in sequence 
        i += 1
        
squareGen = squareGen()

squareGen1 = (i * i for i in range(1, 1000))
print(next(squareGen1))     # get a square value: 1
print(next(squareGen1))     # get a square value: 1
print(next(squareGen1))     # get a square value: 1

#this looks exactly like a comprehension 
#except its surrounded by ()
print(next(squareGen))     # get a square value: 1
print(next(squareGen))     # get 4
print(next(squareGen))     # get 9
print()
   
  

   
###########################################
# 10. lambda (ananymous function ) 
# a. explain the parts of this line of code, and what does it print?
print((lambda x,y : x+y)(2, 3))
#body of the lambda function has to be 1 line 
#prints 5
#2 and 3 are input arguments 
'''

# b. map
def toInch(cm) :
     return cm * 0.3937

def toCm(inch) :
     return inch * 2.54

inches = (2.5, 3,8, 1.0, 10.0)
centimeters = tuple(map(toCm, inches))
#map runs the toCm function for every member of the inches list. returns an iterator 
backToInches = tuple(map(toInch, centimeters))
#converts back to cent. 

print(centimeters)
# write code to convert the centimeter tuple back to inches
print(backToInches)

# c. map with lambda
# write code to do the conversion to centimeters with
# a lambda expression
centimeters = tuple(map(lambda inch : inch *2.54, inches))

print(centimeters)
print()


# d. filter with lambda
origTuple = (1, 10, 2, 30, 5, 7, 45)
# use filter to create a newTuple with origTuple values that are above 10
newTuple = tuple(filter(lambda n : n > 10, origTuple))
print(newTuple)
# do the same with a comprehension
newTuple = tuple([n for n in origTuple if n > 10]) #converts to a list, an then to tuple
newTuple = tuple(n for n in origTuple if n > 10) #makes it a tuple using a generator 
#maps and filters are still in python so people can do funtional code. use comprehension. its better! 
print(newTuple)


'''
# e. sort with lambda
#lamda is used when inout of a function is another function 
list1 = [ [2,9,3], [1,8,4], [6,1,0], [7,5,2] ]
# use the list sort method to sort
list1.sort(key = lambda row : row[1])
print(sorted(list1))

#to sort by 2nd element 
# use the sorted function to sort the list by the 1st element
'''
