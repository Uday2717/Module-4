def find_longest_words(word_list):
    longest_words = []
    max_length = 0
    
    for word in word_list:
        if len(word) > max_length:
            max_length = len(word)
            longest_words = [word]
        elif len(word) == max_length:
            longest_words.append(word)
    
    return longest_words


word_list = ["apple", "banana", "orange", "pineapple", "kiwi", "grapefruit"]
longest_words = find_longest_words(word_list)
print("Longest words:", longest_words)
