# module 1 exercise: modularization
'''
###########################################
# 1. arg packing / unpacking
# a. arg unpacking
def myfunction(x, y, z) :
    print("x is", x, "y is:", y, "z is:", z)
    
myTuple = (1, 2, 3)
# write code to call myfunction and pass to it: 
# - the 3 values in myTuple
myfunction(*myTuple)
# - the value 10 and the last 2 values of myTuple
myfunction(10, *myTuple[1:]) # or myTuple[-2:]

# b. parameter packing
# finish writing the function product:
def product(*args ) :
'''
    
'''
    #multiple args coming in, we pack into one list, and return jsut one value
    result = 1           # init result 
    for num in args :
        result *= num    # keep multiplying the arguments
    return result        # return result

print(product(2,8))
print(product(1,2,3,4))
L = [10,20,30]
print(product(2, L))     # what's printed? 10 20 30 10 20 30
print(product(2, *L))    # what's printed? 2 * 10 * 20 *30


# c. default arg packing/unpacking
def printResult(total = 0, size = 0) :
    print(total, size)
    
printResult(total = 12, size = 10) #will print 12 and 10 

argDict = {'total':12, 'size':10}
# or:
argDict = dict(total = 12, size = 10)  
printResult(**argDict)                #2 key: value pairs are passed to printResult. 2 starts needed for dict unpacking
                                      # this is unpacking into 2 key,value pairs
                                      #for this to work, the dict. must contain the exact same key name, but not the same order
                                      
                                      
def printStudent(id, name, **kwargs) : #only requires 2 arguments
    print('ID', id, '\nName', name)   # print required args
    for k, v in kwargs.items() :      # print what here?
        print(k, v) 

printStudent(1234, 'Lucy', major='psychology')
printStudent(8391, 'Linus', year=2, gpa=3.25)
printStudent(5822, 'Schroeder', year=3, major='music', gpa=4.0)


###########################################
# 2. closure
# which is the closure function? How do you recognize it?
def  add(num) :
        def  add_n(n) :      #closure function: it;'s an innner function and it returns something 
                return num + n
        return add_n       

# what does this code do?
adder = add(10)         
print(adder(2))    #10 + 2     
print(adder(15))    #10 + 15    
adder = add(1)       #rebuilds 
print(adder(2))      #1 + 2   
print()             # blank line

'''


###########################################
# 3. decorator
# what's the name of the closure?
# how is simpleDecorator a decorator?
def simpleDecorator(f) : #accepts a function f of some kind 
    def  wrapper() : #closure
        print('before f runs') #new stuff 
        f() #calls the f function 
        print('after f runs')#new stuff
    return wrapper

@simpleDecorator      #myfunction = simpleDecorator(myfunction)
def myfunction() :    
    print('myfunction runs')

myfunction()     # what is printed?


f2()

#ad decorator on top of the function 

@simpleDecorator
f2()
#then run f2 again

'''
# write a decorator function called trace
# that will print the function name, required args and default args
# before and after the function runs
# apply it to both myfunction and mysort 

def mysort(alist, r=False) :
    alist.sort(reverse=(r==True))
    
mylist = [2, 8, 9, 4]
mysort(mylist)
print(mylist)
mysort(mylist, r=True)
print(mylist)


###########################################
# 4. importing packages
# A. import p1 such that you can:

# call function of each module in p1
# call function c which is in __init__.py


# B. import p2 such that you can:

# call function of each module in p1
# call function c which is in __init__.py


# C. import p3 such that you can:

# call function of each module in p1
# call function c which is in __init__.py

'''