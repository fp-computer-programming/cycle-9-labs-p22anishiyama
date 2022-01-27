# Author: ATN 1/11/21

def add_foods(foods):
    sixth_letter = []
    not_foods = []
    short_foods = []
    for index, food in enumerate(foods):
        try:
            type(food) == str
            sixth_letter.append(food[5])
        except TypeError:
            not_foods.append(food)
        except:
            short_foods.append(food)

    print('sixth_letter:', sixth_letter)
    print('not foods:', not_foods)
    print('short_foods:', short_foods)


add_foods(['potatoes', 'salsa', 'cherries', 'banana', 'apple'])
add_foods(['naan', 'celery', 'buckwheat', 7, 'clementine'])
add_foods(['cheeseburger', True, 'chicken', 'rice', 'radish'])
