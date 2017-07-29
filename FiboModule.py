'''
Created on 29.07.2017

@author: Mario Sikora
'''

if __name__ == '__main__':
    pass

fibonacciarray = [] #declaring global array for fibonacci numbers

def calculate_fibonacci(fibocount): #defining subroutine for filling fibonacci array
    global fibonacciarray #using global array
    j = 3                 #initialising iteration variable  
    
    fibonacciarray.append(1) #initialising array
    fibonacciarray.append(2)    
    
    while j <= fibocount:
        fibonacciarray.append(fibonacciarray[-1]+fibonacciarray[-2])
        j = j + 1

def calculate_retrace(i, j): #subroutine for calculating fibonacci retracement (basically just the ratio)
    print(j/i)
    

calculate_fibonacci(100)   #executing subrouting      
print(fibonacciarray)     #verifiy entries
  
calculate_retrace(fibonacciarray[-1],fibonacciarray[-2]) #calculate retracements
calculate_retrace(fibonacciarray[-1],fibonacciarray[-3])
calculate_retrace(fibonacciarray[-1],fibonacciarray[-4])
calculate_retrace(fibonacciarray[-1],fibonacciarray[-5])

