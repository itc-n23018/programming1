import random

while True:
    letter = chr(random.randint(97, 122))
    print(letter)

    if letter == "s":
        break
