from cs50 import get_string


text = get_string("Text: ")

i = len(text)

letters = 0
words = 1
sentences = 0


for x in range(i):
    c = text[x]
    if c.isalpha():
        letters += 1


    if c == " ":
        words += 1


    if c in [".", "!", "?"]:
        sentences += 1

# Calculation
L = (letters / words) * 100
s = (sentences / words) * 100
subindex = 0.0588 * L - 0.296 * s - 15.8
index = round(subindex)
if index > 16:
    print("Grade 16+")
elif index < 1:
    print("Before Grade 1")
else:
    print(f"Grade {index}")


#back here
