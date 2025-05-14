import numpy as np

"""
Requirements:
- create a main function that can only find the sine of an angle between 0 and 45 degrees ✔️
    - use a loop to generate the values from each term of the polynomial ✔️
    - parameter that sets the degree of the polynomial ✔️
    - only find the value of sine to high precision ✔️
- support functions that calls the main function ✔️
    - cannot use any polynomial approximations ✔️
    - cannot use any pre-existing libraries ✔️
"""
#-----------------------------------------------------------------------------------------------------------------------------------
#Defining pi
pi = np.pi

#-----------------------------------------------------------------------------------------------------------------------------------
#Functions

"""
def sin(x, degree):
    
    def factorial(number):
    
        # This is a function to calculate the factorial of a number by starting from one and multiplying until it reaches the desired number
        
        start = 1
        
        for i in range(1, number + 1, 1):
            # 1st parameter in the range funtion is the starting value
            # 2nd parameter is the last value (not included)
            # 3rd parameter is the increment
    
            start = start * i
            
        return start
    
    i = 1
    
    terms = []
    
    o = round(x/(2*pi))*2*pi
      
    while i <= degree:
        
        denominator = int(factorial(2*i-1))
        
        numerator = (x-o)**(2*i-1)
        
        a = ((-1)**(i-1)) * (numerator/denominator)
        
        terms.append(a)
        
        i = i + 1
        
    return sum(terms)
"""

def int_check(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
    
def float_check(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def bounding(x):
    
    if x > 2*pi:
        minus = False
        
        while not minus:
            if x > 2*pi:
                x = x - 2*pi
            else:
                minus = True
    
    elif x < 0:
        plus = False
        
        while not plus:
            if x < 0:
                x = x + 2*pi
            else:
                plus = True
                
    return x   

"""

def factorial(number):

    # This is a function to calculate the factorial of a number by starting from one and multiplying until it reaches the desired number
    
    start = 1
    
    for i in range(1, number + 1, 1):
        # 1st parameter in the range funtion is the starting value
        # 2nd parameter is the last value (not included)
        # 3rd parameter is the increment

        start = start * i
        
    return start
    
def sin(x, precision):
    
    terms = []
    
    o = round(x/(2*pi))*2*pi
      
    for i in range(1, 1+precision, 1):
        
        denominator = int(factorial(2*i-1))
        
        numerator = (x-o)**(2*i-1)
        
        a = ((-1)**(i-1)) * (numerator/denominator)
        
        terms.append(a)
        
    return sum(terms)

"""
    
def sin(x, precision):
    
    terms = []
    
    o = round(x/(2*pi))*2*pi
      
    for i in range(1, 1+precision, 1):
        
        start = 1
    
        for i in range(1, i + 1, 1):
            # 1st parameter in the range funtion is the starting value
            # 2nd parameter is the last value (not included)
            # 3rd parameter is the increment
    
            start = start * i
        
        denominator = start
        
        numerator = (x-o)**(2*i-1)
        
        a = ((-1)**(i-1)) * (numerator/denominator)
        
        terms.append(a)
        
    return sum(terms)

def answer(x, accuracy):  
    def sqrt(x):
        x = x**0.5
        return x
        
    if (0*pi)/4 <= x <= (1*pi)/4:
        result = sin(x, accuracy)
        
    if (1*pi)/4 < x < (2*pi)/4:
        result = sqrt(1-( sin( (pi/2)-x, accuracy) )**2 )
        
    if (2*pi)/4 < x < (3*pi)/4:
        result = sqrt(1-( sin( x-(pi/2), accuracy) )**2 )
        
    if (3*pi)/4 < x < (4*pi)/4:
        result = sin(pi-x, accuracy)
        
    if (4*pi)/4 < x < (5*pi)/4:
        result = -sin(x-pi, accuracy)
        
    if (5*pi)/4 < x < (6*pi)/4:
        result = -sqrt(1-( sin( (3*pi/2)-x, accuracy) )**2 )
        
    if (6*pi)/4 < x < (7*pi)/4:
        result = -sqrt(1-( sin( x-(3*pi/2), accuracy) )**2 )
        
    if (7*pi)/4 < x < (8*pi)/4:
        result = -sin(2*pi-x, accuracy)
        
        
    return result
          
def cos(x, degree):
    return sin(x + (pi/2), degree)

def tan(x, degree):
    numerator = sin(x, degree)
    denominator = cos(x, degree)
    
    return numerator/denominator

#-----------------------------------------------------------------------------------------------------------------------------------
#Actual display
print("This program finds the values of trignometric functions.")
print("Note: This assumes your vaules are in radians.")

print("")

print("Choose, mortal being!")
print("1) sin(x)")
print("2) cos(x)")
print("3) tan(x)")

print("")

#-----------------------------------------------------------------------------------------------------------------------------------

choice = input("Be not afraid! Enter here: ")

proceed = False

while not proceed:
    
    if int_check(choice):
        choice = int(choice)
        if choice < 1 or choice > 3:
            print("Try again fool.")
            choice = int(input("Enter here once again: "))
        else:
            proceed = True
    else:
        print("YOU DARE FOOL ME, PUNY HUMAN? TRY AGAIN!")
        choice = input("Enter here once again: ")
        proceed = False

print("What is thy angle, mortal!")

angle = input("")

proceed2 = False

while not proceed2:    
    
    if float_check(angle):
        angle = float(angle)
        proceed2 = True
    else:
        print("YOU DARE FOOL ME, PUNY HUMAN? TRY AGAIN!")
        angle = input("Enter here once again: ")
        proceed2 = False

#-----------------------------------------------------------------------------------------------------------------------------------

highest_degree = 13

if choice == 1:
    
    answer = round(sin(angle, highest_degree), 3)
    
    if answer == -0.0:
        answer = 0.0
    
    print(f"Thy answer is {answer}!")
elif choice == 2:
    
    answer = round(cos(angle, highest_degree), 3)
    
    if answer == -0.0:
        answer = 0.0
        
    print(f"Thy answer is {answer}!")    
elif choice == 3:

    answer = round(tan(angle, highest_degree), 3)
    
    if answer == -0.0:
        answer = 0.0
    
    print(f"Thy answer is {answer}!")
