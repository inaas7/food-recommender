from food import Food
from food import RecipeBox

"""This program runs over and over using the while loop until the user enters
 'no' when asked if they want to run the program again."""

prompt = 'yes'
while prompt == 'yes':

    """Each row in the csv file 'food_data' contains details of a food (its 
    name, ingredients, and link to recipe). We read data from the file and store
    each food as an object <Food> in the object recipes which is a RecipeBox.
    """
    foods = RecipeBox()
    with open('food_data.csv', 'r') as file:
        file.readline()
        for line in file:
            info = line.strip().split(',')
            a = Food(info[0], info[1])
            ingredient_list = []
            i = 2
            while i < len(info) and info[i] != '':
                ingredient_list.append(info[i].lower())
                i += 1
            a.add_ingredients(ingredient_list)
            foods.add(a)

    """Now we ask the user whether they want a random recommended recipe, 
    recipes that contain a specific ingredient or ingredients, or recipes that 
    can be made with only the input ingredients. 
    """
    answer = ''

    while not(answer == 'a' or answer == 'a)' or answer == 'b' or answer == 'b)'
              or answer == 'c' or answer == 'c)'):
        answer = input('Select one of the following options (type \'a\', \'b\' '
                       'or \'c\'):\n\na) Do you want a random recommended recip'
                       'e?\nb) Do you want a recipe with a specific ingredient '
                       '(or ingredients)?\nc) Do you want a recipe that you can'
                       ' make with only the ingredients you have?\n')

    """We check to see what the user input and recommend a recipe or recipes 
    accordingly. 
    """
    if answer.lower() == 'a' or answer.lower() == 'a)':
        print(foods.get_random())

    elif answer.lower() == 'b' or answer.lower() == 'b':
        ing = input('Enter list of ingredients separating each ingredient with '
                    'a comma: ').split(',')
        print(foods.has_ingredients(ing))

    else:
        ing = input('Enter list of ingredients separating each ingredient with '
                    'a comma: ').split(',')
        print(foods.has_all_ingredients(ing))

    prompt = input("\nWould you like to run the program again? (Enter 'yes' or "
                   "'no')")
