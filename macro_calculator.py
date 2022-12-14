
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
goal = Food(3200,150,450,100)

food_choices = {"egg": egg,
"sausage": sausage,
"fettuccine": fettuccine,
"pasta bake": pasta_bake,
"dirty fries": dirty_fries,
"banana": banana,
"toast": toast,
"goal": goal}

def get_stats(cals,proteins,carbs,fats,updates):

    food_array = []
    if updates == 0:
        print("What have you eaten? (comma with no spaces)")
    else:
        print("Anything else?")
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
    updates += 1
    print("Calories = {}, Protein = {}, Carbohydrate = {}, Fat = {}".format(cals,proteins,carbs,fats))
    print("Calories = {}, Protein = {}, Carbohydrate = {}, Fat = {}".format(goal.cal,goal.protein,goal.carb,goal.fat))
    get_stats(cals,proteins,carbs,fats,updates)
    return

updates = 0
cals = 0
proteins = 0
carbs = 0
fats = 0

get_stats(cals,proteins,carbs,fats,updates)
