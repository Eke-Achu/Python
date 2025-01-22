from random import randint

def quincunx():
    number_of_balls = int(input("Enter the number of balls to drop: "))
    number_of_slots = int(input("Enter the number of slots in the bean machine: "))

    ball_paths = simulate_path(number_of_balls, number_of_slots)
    
    for i in ball_paths:
        print(i)

    balls = count_R(ball_paths)
    print(balls)
    slots = place_balls(balls, number_of_slots)
    print(slots)
    display_slots(slots)


def simulate_path(number_of_balls, number_of_slots):
    ball_paths = [""] * number_of_balls

    for i in range(number_of_balls):
        current_path = ""

        for j in range(number_of_slots):
            direction = randint(0 , 1)
            char = 'L' if direction == 0 else 'R'

            current_path += char

        ball_paths[i] = current_path

    return ball_paths


def count_R(ball_paths):
    balls = []

    for ball_path in ball_paths:
        count = 0

        for ch in ball_path:
            if ch == 'R':
                count += 1

        balls.append(count)

    return balls


def place_balls(balls, number_of_slots):
    slots = [0] * number_of_slots

    for ball in balls:
        slots[ball] += 1

    return slots


def display_slots(slots):
    most_filled = max(slots)

    for i in range(max(slots)):
        for j in range(len(slots)):
            if slots[j] == most_filled:
                print("0", end = "")
                slots[j] -= 1
            else:
                print(" ", end= "")

        print()   
        most_filled -= 1

def main():
    quincunx()


main()