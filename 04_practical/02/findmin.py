def find_min(list):
    if len(list) == 0:
        return None
    min_value = list[0]
    for value in list:
        if value < min_value:
            min_value = value
            return min_value