'''
Exercise #1
Create a tuple, called Cars, with elements "BMW", "Dodge", and "Ford" in the given order.
'''

Cars = ("BMW", "Dodge", "Ford")


'''
Exercise #2
Access the second element of the Cars tuple.
'''

Cars = ("BMW", "Dodge", "Ford")
Cars[1]


'''
Exercise #3
Call a method that would allow you to extract the provided name and age separately. Then print the name and age values to see if you worked correctly.
'''

name, age = 'Peter,24'.split(',')
print(name, age)


'''
Exercise #4
Create a function called rectangle_info() that takes the length and width of a rectangle as arguments. The function should then return the area and the perimeter of the rectangle. Call the function with arguments 2 and 10 to verify it worked correctly.
'''

def rectangle_info(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter
    

rectangle_info(2, 10)