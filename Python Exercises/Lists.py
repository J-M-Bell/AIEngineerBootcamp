'''
Lists - Exercise #1
Create a list, called Numbers. Let it contain the numbers 10, 25, 40, and 50.
Print the element at index 2 from the list.
'''

Numbers = [10, 25, 40, 50]
print(Numbers[2])


'''
Exercise #2
Print the 0th element from the Numbers list.
'''

Numbers = [10, 25, 40, 50]
print(Numbers[0])


'''
Exercise #3
Print the third-to-last element from the Numbers list using a minus sign in the brackets.
'''

Numbers = [10, 25, 40, 50]
print(Numbers[-3])


'''
Exercise #4
Replace the number 10 with the number 15 in the Numbers list.
'''

Numbers = [10, 25, 40, 50]
Numbers[0] = 15


'''
Exercise #5
Delete the number 25 from the Numbers list.
'''

Numbers = [10, 25, 40, 50]
del Numbers[1]


'''
Using Methods - Exercise #1
Append the number 100 to the Numbers list.
'''

Numbers = [15, 40, 50]
Numbers.append(100)


'''
Exercise #2
With the help of the .extend() method, add the numbers 115 an 140 to the Numbers list.
'''

Numbers = [15, 40, 50, 100]
Numbers.extend([115, 140])


'''
Exercise #3
Print a statement, saying "The fourth element of the Numbers list is" followed by the value of the fourth element of the Numbers list. Ensure you use a trailing comma to concatenate the statement with the value.
'''

Numbers = [15, 40, 50, 100]
Numbers.extend([115, 140])
print("The fourth element of the Numbers list is", Numbers[3])


'''
Exercise #4
Currently, how many elements are there in the Numbers list?
'''


Numbers = [15, 40, 50, 100]
Numbers.extend([115, 140])
print(len(Numbers))