from random import randint

def play_craps():
    roll = roll_dice()
    
    if natural(roll):
        print("You win")
    elif craps(roll):
        print("You lose")
    else: 
        print(f"Point is {roll}")

        next_roll = 0

        while True:
            next_roll = roll_dice()

            if next_roll == 7:
                print("You lose")
                break

            elif next_roll == roll:
                print("You win")
                break


            

def roll_dice():
    num1, num2 = randint(1, 6), randint(1, 6)

    print(f"You rolled {num1} + {num2} = {num1 + num2}")

    return num1 + num2


def natural(number):
    return number == 7 or number == 11

def craps(number):
    return number == 2 or number == 3 or number == 12

def main():
    play_craps()

main()