'''
Python Anonymous Functions - Exercise #1
Define a function called multiply_by_10 that will return a value ten times bigger than the argument.
Apply multiply_by_10 to the argument of 5. Clearly, you should obtain 50.
Please remember to use the print() function to print out the desired output.
'''

def multiply_by_10(x):
    return x * 10
    
print(multiply_by_10(5))


'''
Exercise #2
Using the print() function, write a single line of code that creates and executes a lambda function, returning a value ten times its argument. Use 7 as the input.
'''

print((lambda x: x * 10)(7))


'''
Exercise #3
Define a Lambda function named product_xy that returns the product of two parameters, x and y. Execute it with arguments 4 and 20, respectively.
'''

print((lambda x, y: x * y)(4, 20))


'''
Exercise #4
Create a lambda function that returns the output of the following mathematical expression. Execute it with an argument of 3.
'''

print((lambda x: (((135 - (x ** 3)) ** 4) / ((1 + x) ** 5)))(3))