#CIS 41B LAB ONE
#Logan Kilpatrick 
#1/11/18

class Scores:
    
    def __init__(self):
        '''
        reads in data from the file and stores it in an data structure. 
        no return
        no parameters 

        '''
        self.dataHolder = []
        self.listHolder = []
        try:
            
            defaultFileName = "input1.txt"
            with open(defaultFileName) as f: 
                for line in f:
                    dataSplit = line.split() #Split the data at the white space.  
                    i = 0
                    for item in dataSplit:
                        temp = [dataSplit[i]]
                        temp1 = []
                        self.listHolder.append(temp1)
                        self.dataHolder.append((temp, self.listHolder[i]))
                        i += 1
                    break
                    
            
            with open(defaultFileName) as f: 
                next(f)
                
                for line in f:
                    dataSplit = line.split() #Split the data at the white space.  
                    i = 0
                    for item in dataSplit:
                        temp = dataSplit[i]
                        self.listHolder[i].append(temp)
                        
                        i += 1    
            
        except FileNotFoundError as e: #Input file doesn't exist: print "file not found" message and re-prompt
            print("Can't open " + defaultFileName)       
            raise SystemExit
                
    def getOne(self): # Generator 
        '''
        serves as a generator for the data. It will return one country's
        no parameters
        name and corresponding scores with each next() call

        '''
        
        # data set will have to change to work with sorted names 
        self.dataHolder.sort(key = lambda row : row[0])
        i = 0
        while True :
            yield self.dataHolder[i]  #keyword yield to create next value in sequence 
            i += 1        
    
    
    def printByLast(self):
        
        '''
        prints all countries and all corresponding scores
        no return 
        no paremeters
        prints out directly 

        '''
        import copy
        list2 = copy.deepcopy(self.dataHolder)
        
        list2.sort(key = lambda tup : tup[1][-1], reverse = True)
        for i in range(len(self.dataHolder)):
            temp = list2[i]
            new_data = tuple(' '.join(e) for e in temp)
            #print( ", ".join( repr(e) for e in temp ) )   
            print(new_data[0], ":", new_data[1])
            
    def printMaxMin(self):
        
        '''
        prints the maximum and minimum of all the total scores
        no parameters
        no return 

        '''
        tempNumberHolder = []
        import copy
        list2 = copy.deepcopy(self.dataHolder)
        
        list2.sort(key = lambda tup : tup[1][-1], reverse = True)
        for i in range(len(self.dataHolder)):
            temp = list2[i]
            new_data = tuple(' '.join(e) for e in temp)
            count = new_data[1].split()
            number = 0
            for item in count:
                number += float(item)
            tempNumberHolder.append(number)
            
        print("Max: ", max(tempNumberHolder))  
        print("Min: ", min(tempNumberHolder))                
        