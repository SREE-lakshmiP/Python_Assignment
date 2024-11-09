
text = input("Enter text: ").lower()
words = text.split()
word_freq = {}

for word in words:
    word = word.strip('.,!?"\'')
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

print("Word Frequencies:")
for word, freq in word_freq.items():
    print(f"{word}: {freq}")
