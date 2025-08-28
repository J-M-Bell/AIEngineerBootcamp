'''
Dictionaries - Exercise #1
This is the menu of a close-by restaurant:
Menu = {'meal_1':'Spaghetti', 'meal_2':'Fries', 'meal_3':'Hamburger', 'meal_4':'Lasagna'}
What is the second meal in the list?
'''

Menu = {'meal_1':'Spaghetti', 'meal_2':'Fries', 'meal_3':'Hamburger', 'meal_4':'Lasagna'}

Menu['meal_2']


'''
Exercise #2
Add a fifth meal: "Soup".
'''

Menu = {'meal_1':'Spaghetti', 'meal_2':'Fries', 'meal_3':'Hamburger', 'meal_4':'Lasagna'}

Menu['meal_5'] = "Soup"


'''
Exercise #3
Replace the Hamburger with a Cheeseburger.
'''

Menu = {'meal_1':'Spaghetti', 'meal_2':'Fries', 'meal_3':'Hamburger', 'meal_4':'Lasagna'}

Menu['meal_3'] = "Cheeseburger"


'''
Exercise #4
Attach the Desserts list as a sixth meal (remember, you were supposed to add Soup as a fifth meal earlier!).
'''

Menu = {'meal_1':'Spaghetti', 'meal_2':'Fries', 'meal_3':'Cheeseburger', 'meal_4':'Lasagna'}
Dessert = ['Pancakes', 'Ice-cream', 'Tiramisu']

Menu['meal_5'] = "Soup"
Menu['meal_6'] = Dessert


'''
Exercise #5
Create a new dictionary called Price_list that contains the first five meals of the Menu dictionary as keys and assign the following five values as prices (assumed in dollars): 10, 5, 8, 12, 5. Start by Price_list = {}.
'''

Menu = {'meal_1':'Spaghetti', 'meal_2':'Fries', 'meal_3':'Cheeseburger', 'meal_4':'Lasagna', 'meal_5':'Soup'}

Price_list = {}

Price_list[Menu['meal_1']] = 10
Price_list[Menu['meal_2']] = 5
Price_list[Menu['meal_3']] = 8
Price_list[Menu['meal_4']] = 12
Price_list[Menu['meal_5']] = 5


'''
Exercise #6
Use the print() function and the .get() method to check the price of the Spaghetti in the Price_list.
'''

Price_list = {'Cheeseburger': 8, 'Fries': 5, 'Lasagna': 12, 'Soup': 5, 'Spaghetti': 10}

print(Price_list.get('Spaghetti'))