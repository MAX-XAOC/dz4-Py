from random import randint

my_list = [randint(-10, 10) for _ in range(20)]
uniq_list = [el for el in my_list if my_list.count(el) == 1]
print(f'Начальный спиcок\n{my_list}\nCписок без повторений\n{uniq_list}')
