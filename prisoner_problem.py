from random import shuffle
from time import time

def monte_carlo():
    
    prisoners = [k for k in range(100)] #List of 100 prisoners. 0-99.
    boxes = [k for k in range(100)] #List of 100 boxes. Labeled 0-99.
    shuffle(boxes) #Shuffles the boxes into a random order.
    
    success = 0 #Used to count the succes rate of this process.
                #If it reaches 100 then the prisoners were successful.
    
    for i in range(len(prisoners)):
        guess = prisoners[i] #guess is first set to the current prisoners number. 
        count = 0 #This is the number of boxes the prisoner has checked, the limit is 50.
        
        while count < 50:
            if boxes[guess] == prisoners[i]:
                success += 1
                count = 0
                break
            else:
                guess = boxes[guess]
                count += 1
                
    if success == 100:
        return True
    
def main():
    t1 = time()
    a = 0 #Used to calculate the percentage of successful runs.
    b = 10000 # Number of times to run the code. !WARNING! Large numbers will take time to compute.
    
    for i in range(b):
        if monte_carlo() == True:
            a+=1
    
    t2 = time()
    print("Success Rate = ", (a/b)*100,"%"," ", "Time Taken = %3f" %(t2-t1))
    
        
main()