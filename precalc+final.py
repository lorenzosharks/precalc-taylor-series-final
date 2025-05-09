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

def sin(x, degree):
    
    i = 1
    
    terms = []
       
    def factorial(number):
    
        # This is a function to calculate the factorial of a number by starting from one and multiplying until it reaches the desired number
        
        start = 1
        
        for i in range(1, number + 1, 1):
            # 1st parameter in the range funtion is the starting value
            # 2nd parameter is the last value (not included)
            # 3rd parameter is the increment
    
            start = start * i
            
        return start
        
    while i <= degree:
        
        denominator = int(factorial(2*i-1))
        
        numerator = x**(2*i-1)
        
        a = ((-1)**(i-1)) * (numerator/denominator)
        
        terms.append(a)
        
        i = i + 1
        
    return sum(terms)
      
def cos(x, degree):
    return sin(x + (pi/2), degree)

def tan(x, degree):
    numerator = sin(x, degree)
    denominator = cos(x, degree)
    
    return numerator/denominator

print("This program finds the values of trignometric functions.")
print("Note: This assumes your vaules are in radians.")

print("")

print("Choose, mortal being!")
print("1) sin(x)")
print("2) cos(x)")
print("3) tan(x)")

print("")

choice = int(input("Be not afraid! Enter here: "))
print("What is thy angle, mortal!")
angle = float(input(""))

if choice == 1:
    
    answer = round(sin(angle, 13), 3)
    
    if answer == -0.0:
        answer = 0.0
    
    print(f"Thy answer is {answer}!")
elif choice == 2:
    
    answer = round(cos(angle, 13), 3)
    
    if answer == -0.0:
        answer = 0.0
        
    print(f"Thy answer is {answer}!")    
elif choice == 3:

    answer = round(tan(angle, 13), 3)
    
    if answer == -0.0:
        answer = 0.0
    
    print(f"Thy answer is {answer}!")
