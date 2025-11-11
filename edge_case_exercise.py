def move(my_list, direction):
    if 1 not in my_list:
        return my_list

    new_list = my_list.copy()
    index_of_one = new_list.index(1)

    if direction == 'right':
        if index_of_one < len(new_list) - 1:
            new_list[index_of_one], new_list[index_of_one + 1] = 0, 1

    elif direction == 'left':
        if index_of_one > 0:
            new_list[index_of_one], new_list[index_of_one - 1] = 0, 1

    return new_list
