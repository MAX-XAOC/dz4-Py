from itertools import count, cycle

print('Программа генерирует целвые числа, начиная с указанного. Для генерации  числа необходимо нажать Enter',
      ' для выхода нажмите z')
for i in count(int(input('Введите стартовое число: '))):
    print(i, end='')
    quit = input()
    if quit == 'z':
        break

print('Программа повторяет элементы списка. Для генерации  повторения необходимо нажать Enter, для выхода',
      '  для выхода нажмите z')
u_list = input('Введите список через пробел пробелом: ').split()
iter_ = cycle(u_list)
quit = None

while quit != 'z':
    print(next(iter_), end='')
    quit = input()