def find_max(list):
    if len(list) == 0:
        return None
    max_value = list[0]
    for value in list:
        if value > max_value:
            max_value = value
    return max_value