# Longest Word

sentence = str(input())

words = sentence.split()

long_word_length = len(words[0])

for i in words:
    word_length = len(i)
    if word_length > long_word_length:
        long_word_length = word_length
current_word = i

print(long_word_length)
