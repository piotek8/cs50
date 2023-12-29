def get_int(prompt):
  while True:
    try:
      value = int(input(prompt))
      if 0 < value <= 8:
        return value
      else:
        print("Please enter a positive integer between 1 and 8.")
        print("Try again")
    except ValueError:
      print("Invalid input. Please enter a valid integer.")

def generate_pyramid(height):
  for i in range(1, height + 1):
    spaces = height - i
    blocks = i

    for _ in range(spaces):
      print(" ", end="")

    for _ in range(blocks):
      print("#", end="")

    print()

def main():
  height = get_int("Enter the height of the half-pyramid (from 1 to 8): ")
  generate_pyramid(height)

if __name__ == "__main__":
  main()



