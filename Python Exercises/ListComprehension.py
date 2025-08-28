'''
Python List Comprehensions - Exercise #1
Create the following three lists: products_on_sale, sale_prices, quantities. They should contain the following values respectively:
['Chair_Type_1', 'Chair_Type_2', 'Chair_Type_3', 'Chair_Type_4']
[100, 120, 135, 150]
[1000, 1500, 1300]
'''

products_on_sale = ['Chair_Type_1', 'Chair_Type_2', 'Chair_Type_3', 'Chair_Type_4' ]
sale_prices = [100, 120, 135, 150]
quantities = [1000, 1500, 1300]


'''
Exercise #2
The following code cell will execute a nested loop that will deliver all possible combinations of the elements from the products_on_sale, sale_prices and quantities lists:
for chair_type in products_on_sale:
    for price in sale_prices:
        for quantity in quantities:
            print ([chair_type, price*quantity])
Use a list comprehension to obtain the same output. Store it in a variable called sales_revenue.
Make sure you refrain from obtaining any inexistent "None" values.
'''

products_on_sale = ['Chair_Type_1', 'Chair_Type_2', 'Chair_Type_3', 'Chair_Type_4' ]
sale_prices = [100, 120, 135, 150]
quantities = [1000, 1500, 1300]


sales_revenue = filter(None, [print(chair_type, price*quantity)
                 for chair_type in products_on_sale
                 for price in sale_prices 
                 for quantity in quantities])
				
				
'''
Exercise #3
Use a list comprehension to return a list with all even numbers between 1 and 10 inclusive, multiplied by 10.
Please remember to use the print() function to print out the desired output.
'''

print([num * 10 for num in range(1, 11) if num % 2 == 0])



'''
Exercise #4
We consider the previous answer as the Pythonic way to obtain the output because it involved the use of a list comprehension.
Can you devise a method to achieve the same output—returning a list with all even numbers between 1 and 10, inclusive, each multiplied by 10—using a "non-Pythonic" approach, specifically without employing list comprehensions?
'''

for n in range(1, 11):
    if n % 2 ==  0:
        print(n * 10, end = " ")
		
		
'''
Exercise #5
Using list comprehension, return a list that contains the element from range(1, 11) multiplied by 10 if the number is even, and "None" if that number is odd.
Please use num as an iteration variable name in the required list comprehension.
'''

print([num * 10 if num % 2 == 0 else 'None' 
            for num in list(range(1, 11))])
			
