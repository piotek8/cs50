from cs50 import get_int

while True:
    x = get_int("Height: ")
    if x >= 1 and x <= 8:
        break

for i in range(x):
    print(" " * (x - 1 - i), end="")
    print("#" * (i + 1))
