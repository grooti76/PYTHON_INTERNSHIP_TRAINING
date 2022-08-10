import random
# num = random.randint(0, 9)
# print(num)


def sgw(com, mine):
    if (com == mine):
        return None
    elif(com == 's' and mine == 'g'):
        return True
    elif(com == 'w' and mine == 's'):
        return True
    elif(com == 'g' and mine == 'w'):
        return True
    else:
        return False


choice = ('s', 'w', 'g')
com = random.randint(0, 2)
com = choice[com]
mine = input("Choose either w or g or s\n")
win = sgw(com, mine)
print(f"you choose {mine} and computer choose {com}")

if win is None:
    print("Match Draw")
elif win is True:
    print("You Win")
else:
    print("You Lose")
