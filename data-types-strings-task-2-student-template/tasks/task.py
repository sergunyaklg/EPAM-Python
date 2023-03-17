def get_longest_word( s: str) -> str:
    # split the string by whitespaces
    words = s.split()
    # return the word with the maximum length
    return max(words, key=len)