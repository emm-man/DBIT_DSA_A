def count_char_frequencies(s):
    """
    Counts character frequencies in the given string using a dictionary.
    """
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

# Example usage:
if __name__ == "__main__":
    text = "data structures and algorithms"
    frequencies = count_char_frequencies(text)
    print(frequencies)