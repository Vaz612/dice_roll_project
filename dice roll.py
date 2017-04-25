import random
import sys

Roll = "null"
while Roll != "Roll":
    print ("Please type Roll!")
    Roll = input()
    if Roll != "Roll":
        print("Are you sure you want to play? Please type Yes or No!")
        response = input()
        if response == "Yes" or response == "yes":
            continue
        elif response == "No" or response == "no":
            sys.exit()


die_1 = random.randint(1, 6)
die_2 = random.randint(1, 6)
dice_total = die_1 + die_2
print("You rolled " + str(dice_total) + " (" + str(die_1) + " + " + str(die_2) + ")!")
