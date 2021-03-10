def create_cook_book(dish_list):
    cook_book = {}
    for dish in dish_list:
        nlst = dish.split('\n')
        # print(nlst)
        dishes = nlst[0]
        count = int(nlst[1])
        ingr_list = []
        for i in range(count):
            ingr_dic = {}
            ingr = nlst[2 + i].split(' | ')
            ingr_dic['ingredient_name'] = ingr[0]
            ingr_dic['quantity'] = ingr[1]
            ingr_dic['measure'] = ingr[2]
            ingr_list.append(ingr_dic)
        cook_book[dishes] = ingr_list
    return cook_book