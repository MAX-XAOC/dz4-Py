my_list = [11, 133, 21, 2, 7, 7, 5, 4,55, 0]
more_then = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]
print(more_then)