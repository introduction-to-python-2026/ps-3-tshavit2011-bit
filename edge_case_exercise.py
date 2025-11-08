def move(my_list, direction=None):
    if 1 not in my_list:
        return my_list

    index = my_list.index(1)
    new_list = my_list.copy()

    if direction == 'right' and index < len(my_list) - 1:
        new_list[index], new_list[index + 1] = 0, 1
    elif direction == 'left' and index > 0:
        new_list[index], new_list[index - 1] = 0, 1

    return new_list
