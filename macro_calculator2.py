
import numpy as np
class Food:
    def __init__(self, cal, protein, carb, fat):
        self.cal = cal
        self.protein = protein
        self.carb = carb
        self.fat= fat

egg = Food(70,7,0.6,5)
sausage = Food(100,15,10,12)
fettuccine = Food(592,33.1,58.1,24.3)
pasta_bake = Food(680,36,60,32)
dirty_fries = Food(1106,36,86,66)
banana = Food(110,1,28,0)
toast = Food(134,4.9,18.2,4.1)

food_choices = {"egg": egg,
"sausage": sausage,
"fettuccine": fettuccine,
"pasta bake": pasta_bake,
"dirty fries": dirty_fries,
"banana": banana,
"toast": toast}

def daily_stats():
    cals = 0
    proteins = 0
    carbs = 0
    fats = 0

    food_array = []
    print("What have you eaten? (comma with no spaces)")
    user_list = input()
    food_array = [item for item in user_list.split(",")]

    for i in range(len(food_array)):
        get_food = food_choices.get(food_array[i], None)  # Get the chosen class, or None if input is bad
        if get_food is None:
            print("item {} is invalid".format(i+1)) # They entered bad input that doesn't correspond to a food
        else:
            cals += get_food.cal
            proteins += get_food.protein
            carbs += get_food.carb
            fats += get_food.fat
    return print("Calories = {}, Protein = {}, Carbohydrate = {}, Fat = {}".format(cals,proteins,carbs,fats))
'''
def add_food():
    food_name = input("Food:")
    macros = input("Input macros:")
    macro_array = [item for item in macros.split(",")]

    globals()[food_name] = Food(macro_array[0],macro_array[1],macro_array[2],macro_array[3])
    food_choices[food_name] = food_name

add_food()
'''
