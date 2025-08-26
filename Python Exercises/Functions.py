'''
Exercise #1
Define a function called multiplication_by_2(x) that returns a value equal to its argument multiplied by 2.
'''

def multiplication_by_2(x):
    return x * 2


'''
Exercise #2
Define a function called division_by_2(x) that returns a float value equal to its argument divided by 2.
'''

def division_by_2(x):
    return float(x) / 2
	
	
'''
Exercise #1
Define a function called exponentiation_exp_2(x) that states the value of the argument accompanied by the phrase "Raised to the power of 2:" and returns a value equal to its argument raised to the power of 2. This time, use a new variable, called result, in the body of the Function. Call the function with some argument to verify it works properly.
'''

def exponentiation_exp_2(x):
    result = x ** 2
    print(f"{x} Raised to the power of 2:")
    return result
    
    
exponentiation_exp_2(10)


'''
Exercise #1
Define a function called plus_five() that adds 5 to its argument. Then, define another function named m_by_3() that multiplies the argument (the result obtained from plus_five()) by 3. Verify your code was correct by calling the second function with an argument of 5. Was your output equal to 30?
'''

def plus_five(x):
    return x + 5
    

def m_by_3(x):
    return plus_five(x) * 3
    
m_by_3(5)


'''
Combining Conditional Statements and Functions - Exercise #1
Define a function, called compare_the_two(), with two arguments. If the first one is greater than the second one, let it print "Greater". If the second one is greater, it should print "Less". Let it print "Equal" if the two values are the same number.
'''

def compare_the_two(x1, x2):
    if x1 > x2:
        print("Greater")
    elif x1 < x2:
        print("Less")
    else:
        print("Equal")
        

'''
Notable Built-in Functions in Python - Exercise #1
Obtain the maximum number among the values 25, 65, 890, and 15.
'''

max(25, 65, 890, 15)


'''
Exercise #2
Obtain the minimum number among the values 25, 65, 890, and 15.
'''

min(25, 65, 890, 15)


'''
Exercise #3
Find the absolute value of -100.
'''

abs(-100)


'''
Exercise #4
Round the value of 55.5.
'''

round(55.5)


'''
Exercise #5
Round 35.56789 to the third digit.
'''

round(35.56789, 3)


'''
Exercise #6
Find the sum of all elements in the provided list, called "Numbers".
'''

Numbers = [1, 5, 64, 24.5]
sum(Numbers)


'''
Exercise #7
Use a built-in function to raise 10 to the power of 3.
'''

pow(10, 3)


'''
Exercise #8
In one line of code, find how many characters there are in the word "Elephant"?
'''

len("Elephant")


'''
Exercise #9
Create a function, called distance_from_zero(), that returns the absolute value of a provided single argument and prints a statement "Not possible" if the argument provided is not a number. To solve the task, use the type() function in the body of distance_from_zero().
Call the function with the values of -10 and "cat" to verify it works correctly.
'''

def distance_from_zero(x):
    if type(x) == int:
        return abs(x)
    else:
        print("Not possible")
        

distance_from_zero(-10)
distance_from_zero("cat")