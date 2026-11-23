text = input("Enter a sentence:") or "I Love learning Python"

print("Length=", len(text))
print("Characters in the given text:")

for ch in text:
    print(ch,end = ",")