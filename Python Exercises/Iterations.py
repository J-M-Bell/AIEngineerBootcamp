'''
For Loops - Exercise #1
Create a For loop that prints every digit on a new line.
'''

digits = [0,1,2,3,4,5,6,7,8,9]
for n in digits:
    print(n)


'''
Exercise #2
Adjust the code, so the digits are all printed on the same line.
'''

digits = [0,1,2,3,4,5,6,7,8,9]

for d in digits:
    print (d, end = " ")
	
	
'''
While Loops and Incrementing - Exercise #1
Create a while loop that will print all odd numbers from 0 to 30 on the same row.
'''

x = 1
while x < 30:
    print(x, end = " ")
    x += 2
	

'''
Create Lists with the range() Function - Exercise #1
Use the range() function to create a list with all numbers from 1 to 10.
'''

list(range(1, 11))


'''
Exercise #2
Use the range() function to create a list with all numbers from 0 to 19.
'''

list(range(20))


'''
Exercise #3
Use the range() function to create a list with all even numbers from 0 to 30 included.
'''

list(range(0, 31, 2))


'''
Conditional Statements and Loops - Exercise #1
Create a For loop that will print all the variables from a given list multiplied by 2. Let the list contain all numbers from 1 to 10. Create it with the help of the range() function.
'''

x_list = list(range(1, 11))
for x in x_list:
    print(x * 2)
    
    
'''
Exercise #2
Create a small program that runs a loop over all values from 1 to 30. Let it print all odd numbers on the same line, and in the place of the even numbers, it should print "Even". Use the range() function to help solve this exercise.
'''

for x in range(1, 31):
    if x % 2 == 0:
        print("Even", end = " ")
    else:
        print(x, end = " ")
        
        
'''
Exercise #3
You have the following list of numbers. Iterate over this list, printing out each list value multiplied by 10. Find two solutions of this problem.
'''

n = [1,2,3,4,5,6]
for x in n:
    print(x * 10, end = " ")
    
for x in range(len(n)):
    print(n[x] * 10, end = " ")
    
    
'''
Conditional Statements, Functions, and Loops - Exercise #1
You are provided with the nums list. Define a function called count() containing a while loop to count the number of values in the nums list that are lower than 20.
'''

nums = [1,35,12,24,31,51,70,100]

def count(numbers):
    x = 0
    total = 0
    while x < len(numbers):
        if numbers[x] < 20:
            total += 1
        x += 1
    return total
    
count(nums)
        

'''
Iterating over Dictionaries - Exercise #1
In this exercise you will use the same dictionaries as the ones we used in the lesson - prices and quantity. This time, don't just calculate all the money Jan spent. Calculate how much she spent on products with a price of 5 dollars or more.
'''

prices = {
    "box_of_spaghetti" : 4,
    "lasagna"  : 5,
    "hamburger" : 2
   }
quantity = {
    "box_of_spaghetti" : 6,
    "lasagna"  : 10,
    "hamburger" : 0
    }

money_spent = 0

for i in prices:
    if prices[i] >= 5: 
        money_spent += (prices[i] * quantity[i])

print(money_spent)


'''
Exercise #2
How much did Jan spent on products that cost less than 5 dollars?
'''

prices = {
    "box_of_spaghetti" : 4,
    "lasagna"  : 5,
    "hamburger" : 2
   }
quantity = {
    "box_of_spaghetti" : 6,
    "lasagna"  : 10,
    "hamburger" : 0
    }

money_spent = 0

for i in prices:
    if prices[i] < 5: 
        money_spent += (prices[i] * quantity[i])

print(money_spent)
