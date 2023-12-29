import sys
from pyfiglet import Figlet
from random import choice

figlet = Figlet()


if len(sys.argv) == 1:
    figlet.setFont(font=choice(figlet.getFonts()))
    print("Output:", figlet.renderText(input("Input: ")), sep="\n")

elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
    figlet.setFont(font=sys.argv[2])
    print("Output:", figlet.renderText(input("Input: ")), sep="\n")

else:
    sys.exit("Invalid usage")



'''
from pyfiglet import Figlet
import sys
import random


figlet = Figlet()

if len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
    random_answer = True
elif len(sys.argv) == 1:
    random_answer = False
else:
    sys.exit(1)

figlet.getFonts()


if random_answer == False:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        print('Invalid usage')
        sys.exit(1)
else:
    font = random.choice(figlet.getFonts())

msg = input('Input: ')

print('Output:')
print(figlet.renderText(msg))
'''
