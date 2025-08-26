'''
Exercise #1
Create a two-line code that prints "The condition has been satisfied" if 5 is greater than 2.
'''

if 5 > 2:
    print("The condition has been satisfied")
	

'''
Exercise #2
Assign 10 to the variable x and 25 to the variable y. In the same cell, create 2 conditional statements. Let the first one print "Both conditions are correct" if x is greater then 3 and y is greater than 13. Let the second one print "At least one of the conditions is false" if x is less than or equal to 3 or y is less than or equal to 13. Change the values assigned to x and y and re-run the cell to verify your code still works.
'''

x = 10
y = 25

if x > 3 and y > 13:
    print("Both conditions are correct")
    

if x <= 3 or y <= 13:
    print("At least one of the conditions is false")
	
	
'''
The ELSE Statement - Exercise #1
Let x represent the number of orders received during a certain day. Create a program that prints "A busy day" if x is greater than 100, and "A calm day" otherwise.
'''

x = 10
if x > 100:
    print("A busy day")
else:
    print("A calm day")
	

'''
The ELIF Statement - Exercise #1
Create the following piece of code: If x > 200, print out "Big"; If x > 100 and x <= 200, print out "Average"; and If x <= 100, print out "Small". Use the if, elif, and else keywords in your code.
'''

x = 10

if x > 200:
    print("Big")
elif x > 100 and x <= 200:
    print("Average")
else:
    print("Small")
	
	
'''
Exercise #2
Keep the first two conditions of the code from the previous exercise (if x > 200, print out "Big"; If x > 100 and x <= 200, print out "Average").
Add a new elif statement, so that, eventually, the program prints "Small" if x >= 0 and x <= 100, and "Negative" if x < 0.
'''

x = 10

if x > 200:
    print("Big")
elif x > 100 and x <= 200:
    print("Average")
elif x >= 0 and x <= 100:
    print("Small")
else:
    print("Negative")