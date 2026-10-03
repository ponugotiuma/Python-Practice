# Find the longest word in a sentence.
sentence="Hello World! Python Programming's beginner code"
words=sentence.split()
longest=words[0]
for word in words:
    if len(word)>len(longest):
        longest=word
print(longest)
