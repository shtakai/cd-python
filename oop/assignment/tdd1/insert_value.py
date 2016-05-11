def insert_value_at(index, my_list, value):
    if index >= len(my_list) + 1 or index < 0:
        return False

    my_list.insert(index, value)
    return my_list
