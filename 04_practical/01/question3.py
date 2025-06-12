def countdown_head_recursion(n):
    """
    Prints numbers from n down to 0 using head recursion.
    """
    if n < 0:
        return
    print(n)
    countdown_head_recursion(n - 1)

# Example usage:
if __name__ == "__main__":
    countdown_head_recursion(5)
    # Output: 5 4 3 2 1 0