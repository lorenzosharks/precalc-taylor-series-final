import numpy as np
pi = np.pi

def sin(x, precision):
    
    terms = []
    
    o = round(x/(2*pi))*2*pi
      
    for i in range(1, 1+precision, 1):
                
        start=1
        b=1
        
        for b in range(1, 2*i, 1):
            # 1st parameter in the range funtion is the starting value
            # 2nd parameter is the last value (not included)
            # 3rd parameter is the increment
            
            print(start)
            
            start = start * b
            
        
        #print(start)
        
        denominator = start
        
        numerator = (x-o)**(2*i-1)
        
        #print(numerator)
        
        
        a = ((-1)**(i-1)) * (numerator/denominator)
        
        #print(a)
        
        terms.append(a)

        
    return sum(terms)

print(sin(10,10))