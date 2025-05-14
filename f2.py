import numpy as np
pi = np.pi

def factorial(number):

    # This is a function to calculate the factorial of a number by starting from one and multiplying until it reaches the desired number
    
    start = 1
    i=1
    
    for i in range(1, number + 1, 1):
        # 1st parameter in the range funtion is the starting value
        # 2nd parameter is the last value (not included)
        # 3rd parameter is the increment

        print(start)

        start = start * i
        
    return start
    
def sin(x, precision):
    
    terms = []
    
    o = round(x/(2*pi))*2*pi
      
    for i in range(1, 1+precision, 1):
                
        denominator = factorial(2*i-1)
        
        #print(denominator)
        
        numerator = (x-o)**(2*i-1)
        
        #print(numerator)

        a = ((-1)**(i-1)) * (numerator/denominator)
        
        #print(a)
        
        terms.append(a)
                
    return sum(terms)

print(sin(10,10))