rent = 1050
moneySaved = 12643

if (moneySaved - (rent * 12)) < 0:
    print("You do not have enough money for a year of rent! Keep saving!")
else:
    if (moneySaved % 12) != 0:
        print("Yay! You have extra money saved up!")
    elif (moneySaved % 12) == 0:
        print("Well, at least you have enough money for rent this year!")
