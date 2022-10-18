import numpy as np
class Food:
    def __init__(self, cal, protein, carb, fat):
        self.cal = cal
        self.protein = protein
        self.carb = carb
        self.fat= fat

egg = Food(70,7,0.6,5)
'''egg.cal = 70
egg.protein = 7
egg.carb = 0.6
egg.fat = 5'''

def daily_stat():
    print("What have you eaten today?")
    food_array = list(input())
    '''cals = 0
    proteins = 0
    carbs = 0
    fats = 0
    
    for i in range(len(food_array)):
        instance = food_array[i]
        cals += instance.cal
        proteins += instance.protein
        carbs += instance.carb
        fats += instance.carb

    return cals, proteins, carbs, fats'''
    return print(food_array)
daily_stat()