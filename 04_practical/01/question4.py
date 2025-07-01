def sum_tail_recursion(n, acc=0):
    """
    Returns the sum of all numbers from 0 to n using tail recursion.
    """
    if n == 0:
        return acc
    return sum_tail_recursion(n - 1, acc + n)

# Example usage:
if __name__ == "__main__":
    print(sum_tail_recursion(5))  # Output: 15 (5+4+3+2+1+0)