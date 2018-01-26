# CIS 41B Assignment 1
# Name: Logan Kilpatrick 
#1/12/18


from scores import Scores
    
def main() :
    data = Scores()     # create Scores object
    gen = data.getOne()   # create generator object
    print(next(gen))    # fetch first data of object
    data.printByLast()  # print all data sorted by last field
    print(next(gen))    # fetch next data of object
    data.printMaxMin()  # print the max and min of the total scores
    
    print(next(gen))    # fetch next data of object
    print(next(gen))    # fetch next data of object
    print(next(gen))    # fetch next data of object
    print(next(gen))    # fetch next data of object
    #fixed issue with generator using for loop! 
   
    
main()