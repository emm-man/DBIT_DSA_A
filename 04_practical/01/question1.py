def reverse_list(lst):
    """
    Returns a new list that is the reverse of the input list.
    """
    return lst[::-1]

def rotate_list(lst, k):
    """
    Rotates the list to the right by k positions.
    """
    n = len(lst)
    k = k % n  # handle rotations greater than list length
    return lst[-k:] + lst[:-k]

# Example usage:
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print("Reversed:", reverse_list(my_list))      # [5, 4, 3, 2, 1]
    print("Rotated by 2:", rotate_list(my_list, 2)) # [4, 5, 1, 2, 3]