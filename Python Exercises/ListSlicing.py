'''
List Slicing - Exercise #1
Using list slicing, obtain the numbers 100 and 115.
'''

Numbers = [15, 40, 50, 100, 115, 140]
Numbers[3:5]


'''
Exercise #2
Using slicing, extract the first four elements from the list.
'''

Numbers = [15, 40, 50, 100, 115, 140]
Numbers[:4]


'''
Exercise #3
Using slicing, extract all the elements from the list from the 3rd position onwards.
'''

Numbers = [15, 40, 50, 100, 115, 140]
Numbers[3:]


'''
Exercise #4
Using slicing, extract the last 4 elements from the list.
'''

Numbers = [15, 40, 50, 100, 115, 140]
Numbers[-4:]


'''
Exercise #5
Which is the position of the value 15?
'''

Numbers = [15, 40, 50, 100, 115, 140]
Numbers.index(15)


'''
Exercise #6
Create a list, called Two_Numbers. Let its elements be the values 1 and 2. Then, create a new one, named All_Numbers, that will contain both the Two_Numbers and the Numbers lists in the given order.
'''

Numbers = [15, 40, 50, 100, 115, 140]
Two_Numbers = [1, 2]
All_Numbers = [Two_Numbers, Numbers]


'''
Exercise #7
Sort all the numbers in the Numbers list from the largest to the smallest.
'''

Numbers = [15, 40, 50, 100, 115, 140]
Numbers.sort(reverse=True)

