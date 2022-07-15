import pprint
import os

#  Task 1

def get_dict_for_ingredients(strk):
    ingredient_name, quantity, measure = strk.split(' | ')
    quantity = int(quantity)
    return {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}


def get_cook_book():
    name = input('Ввудите имя файла или путь к файлу: ')
    with open(name, 'r', encoding='utf-8') as file:
        cook_book = {}
        for line in file:
            ingr_list = []
            name = line.strip()
            num = int(file.readline().strip())
            for _ in range(num):
                ingr = file.readline().strip()
                ingredient = get_dict_for_ingredients(ingr)
                ingr_list.append(ingredient)
            cook_book[name] = ingr_list
            file.readline()
    return cook_book

## VERSION 2:

# def get_recepts_from_file(name):
#     with open(name, 'r', encoding='utf-8') as file:
#         lst = file.readlines()
#
#     lst1 = [i.strip() for i in lst]
#     recepts_number = lst1.count('')
#     res = []
#     for i in range(recepts_number):
#         indx = lst1.index('')
#         res.append(lst1[:indx])
#         del lst1[:indx + 1]
#     res.append(lst1)
#     return res
#
#
# def get_dict_for_ingredients(strk):
#     ingredient_name, quantity, measure = strk.split(' | ')
#     quantity = int(quantity)
#     return {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}
#
#
# def get_cook_book():
#     name = input('Ввудите имя файла или путь к файлу: ')
#     dish_list = get_recepts_from_file(name)
#     cooking_book = {}
#     for dish in dish_list:
#         cooking_book[dish[0]] = [get_dict_for_ingredients(ingredient) for ingredient in dish[2:]]
#     return cooking_book


cook_book = get_cook_book()
pprint.pprint(cook_book, width=120, sort_dicts=False)

print()
print('*-*' * 30, '\n')


#############################################################################################

# Task 2
def get_shop_list_by_dishes(dishes: list, person_count: int):
    ingredient_needed = {}
    for dish in dishes:
        if dish in cook_book:

            for ingr in cook_book[dish]:
                if ingr['ingredient_name'] not in ingredient_needed:
                    ingredient_needed[ingr['ingredient_name']] = {"quantity": ingr['quantity'] * person_count,
                                                                  'measure': ingr['measure']}
                else:
                    ingredient_needed[ingr['ingredient_name']]['quantity'] += ingr['quantity'] * person_count

    return ingredient_needed


pprint.pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2), width=80, sort_dicts=False)

print('*-*' * 30, '\n')
#######################################################################################
# Task 3

# PATH = os.getcwd()
# SUB = 'homework'
# FULL_PATH = os.path.join(PATH, SUB)
FULL_PATH = input('Введите путь к папке с файлами для сортировки: ')
file_list = os.listdir(path=FULL_PATH)
files_dict = {}
for file in file_list:
    with open(FULL_PATH + '\\' + file, 'r', encoding='UTF-8') as f:
        content = f.readlines()
        files_dict[file] = (len(content), content)
files_dict_sorted = dict(sorted(files_dict.items(), key = lambda x: x[1]))
with open('result.txt', 'w', encoding='UTF-8') as result:
    for key, volume in files_dict_sorted.items():
        result.write(key + '\n')
        result.write(str(volume[0]) + '\n')
        result.writelines(volume[1])
        if not volume[1][-1].endswith('\n'):
            result.write('\n')
