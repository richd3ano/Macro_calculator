import numpy as np
class Food:
    def __init__(self, cal, protein, carb, fat):
        self.cal = cal
        self.protein = protein
        self.carb = carb
        self.fat= fat

egg = Food(70,7,0.6,5)
sausage = Food(100,15,10,12)

food_choices = {"egg": egg,
"sausage": sausage}

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

daily_stats()