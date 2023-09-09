'''
Aditya Chakraborty
9/7/23
Cyber Dice
'''
import random
input("Press enter to roll")

r = random.randint(1,6)

print(f"You rolled a {r}")

running = True
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while running:
    option = input("Press enter to roll again, or press any letter to quit: ")
    if option in alphabet:
        running = False
        print("Goodbye!")
        break
    t = random.randint(1,6)
    print(f"You rolled a {t}")
    
