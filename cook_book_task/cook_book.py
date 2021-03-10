import os
from pprint import pprint
from create_cookbook import create_cook_book

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingr in cook_book[dish]:
            shop_ingr = ingr['ingredient_name']
            ingr.pop('ingredient_name')
            ingr['quantity'] = int(ingr['quantity']) * person_count
            if shop_ingr not in shop_list:
                shop_list[shop_ingr] = ingr
            else:
                quant = int(ingr['quantity'])
                shop_list[shop_ingr]['quantity'] += quant
    return shop_list

file_path = os.path.join(os.getcwd(), 'recipes.txt')

with open(file_path, 'r') as f:
    dish_list = f.read().split('\n\n')

dishes = (input('Ведите блюда через ,: '))
dishes = dishes.split(', ')
person_count = int(input('Введите количество персон: '))

cook_book = create_cook_book(dish_list)
pprint(cook_book)

shop_list = get_shop_list_by_dishes(dishes, person_count)
pprint(shop_list)