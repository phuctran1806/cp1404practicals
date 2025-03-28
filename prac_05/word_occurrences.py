"""
Word Occurrences
Estimate: 20 minutes
Actual: 10 minutes
"""
from operator import itemgetter

word_to_count = {}

input_string = input("Text: ")
for word in input_string.split():
    word_to_count[word] = word_to_count.get(word, 0) + 1

width = max((len(word) for word in word_to_count.keys()))

for word, count in sorted(word_to_count.items(), key=itemgetter(0)):
    print(f"{word:{width}} : {count}")
