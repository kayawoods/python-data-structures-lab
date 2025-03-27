# Exercise 1: List and Indexing
#
# Create a list named students containing at least three student names (strings).
# Assign the second student’s name to a variable named first_student.
# Assign the last student’s name to a variable named last_student.

def manage_students():
    students = ['Kaya', 'Mica', 'Kiera']
    first_student=students[1]
    last_student=students[2]
    return first_student, last_student

# Call the function and print the result
print('Exercise 1:', manage_students())

# Exercise 2: Loop and String Concatenation
#
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Create a variable named meal and assign an empty string to it.
# Use a for loop to iterate over the strings in foods and append each string to meal.

def combine_foods():
    foods = ('cheese', 'asparagus','broth')
    meal = ''
    for food in foods: 
        meal += food + ', '
    return(meal)

print('Exercise 2:', combine_foods())

# Exercise 3: Slicing Tuples
#
# Using the slice operator, assign a new tuple containing only the last two food strings in the foods to a variable named last_two_foods.

def slice_foods():
    foods = ('cheese', 'asparagus','broth')
    last_two_foods = slice(1,3)
    return(foods[last_two_foods])

# Call the function and print the result
print('Exercise 3:', slice_foods())

# Exercise 4: Dictionaries and String Formatting
#
# Create a dictionary named home_town containing the keys of city, state, and population.
# Using the home_town dictionary, assign to a variable named home_town_message a string with this format: “I was born in <city>, <state> - population of <population>”



def hometown_info():
    home_town = {
    'City': 'Albuquerque',
    'State': 'New Mexico',
    'Population': 'IDK'
    
   }
    home_town_message = f' I was born in {home_town['City']}, {home_town['State']} - population of {home_town['Population']}'
    return home_town_message
# Call the function and print the result
print('Exercise 4:', hometown_info())

# Exercise 5: Iterating Over Dictionary Items
#
# Define an empty list named home_town_items.
# Use a for loop to iterate over the key: value pairs in the home_town dictionary and append a string with the following format to home_town_items: "<key> = <value>"

def list_home_town_items():
    home_town = {
    'City': 'Albuquerque',
    'State': 'New Mexico',
    'Population': 'IDK'
   }
    home_town_items = [] 
    for key, val in home_town.items():
        home_town_items.append(f" {key} = {val}")
    return home_town_items
    
print('Exercise 5:', list_home_town_items())
