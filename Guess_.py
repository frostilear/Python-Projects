import time
import random
while True:
    print("")
    print("Enter a guess of a number from 0 to 10.")
    print("So what do you think it will be?")
    y = random.randrange(0, 11)
    x = int(input())
    if x > 10 or x < 0:
        print("You thought you are smart,eh?.Well enter a valid number next time.")
    elif x == y:
        print("Incredible Job!,you guessed the correct number, today could be your lucky day?")
    elif x != y:
        print("Tough luck,try again next time bud.")
        time.sleep(3)
        print("Do you wanna know what the number was just for fun?")
        z = input().lower()
        if z == "yes":
            print("the number was:", y)
            time.sleep(0.6)
            continue
        elif z == "no":
            print("Ok fine...")
            time.sleep(0.6)
            continue
        else:
            print("What did you do there? I only expected a yes or a no.")
            time.sleep(0.6)
            continue