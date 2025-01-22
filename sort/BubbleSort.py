def bubbleSort(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp


def sort():
    lineInput = input("Enter ten integers: ").strip()
    numbers = [int(x) for x in lineInput.split()]

    bubbleSort(numbers)

    print("The sorted numbers are:", end = " ")
    for i in numbers:
        print(i, end = " ")

    print()


def main():
    sort()


main()
                