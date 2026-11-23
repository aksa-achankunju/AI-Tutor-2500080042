word = input("Enter a word:") or "Python"

print("word=",word)
print("Length of the word:",len(word))

Characters = list(word)
print("Characters in the given word:",Characters)
pairs = list(zip(Characters,range(len(Characters[1:]))))

print("Adjacent pairs:",pairs)