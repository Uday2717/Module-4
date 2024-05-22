from collections import Counter
def word_frequency(fname):
        with open(fname) as f:
                return Counter(f.read().split())

print("Number of words in the file :",word_frequency("text.txt"))
