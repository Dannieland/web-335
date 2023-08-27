#----------------------------------------------------------
# taplin_calculator.py
# Danielle Taplin
# 08/26/23
# code to calculate numerical values
#----------------------------------------------------------

#declare function adding two parameters together
def add(x,y):
    #return the sum of the parameters x and y
    return x + y

#declare function subtracting one parameter from the other
def subtract(x,y):
    #return the difference of the parameter y subtracted from x
    return x - y

#declare a function multiplying two parameters together
def multiply(x,y):
    #return the product of x multiplied by y
    return x * y

#declare a function dividing two parameters
def divide(x,y):
    #return the quotient of x divided by y
    return x / y


#declare two integer variables for testing the calculation functions
num1 = 10
num2 = 5

#call four calculation functions and store the results in string variables
add_result = str(num1) + " + " + str(num2) + " is " + str(add(num1, num2))
subtract_result = str(num1) + " - " + str(num2) + " is " + str(subtract(num1, num2))
multiply_result = str(num1) + " x " + str(num2) + " is " + str(multiply(num1, num2))
divide_result = str(num1) + " / " + str(num2) + " is " + str(divide(num1, num2))

#print calculation results variables to the console
print(add_result)
print(subtract_result)
print(multiply_result)
print(divide_result)