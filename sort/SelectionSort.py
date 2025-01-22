def selectionSort(list):
    copy = [] + list

    for i in range(len(list)):
        indexOfMax = list.index(max(copy))

        temp = list[len(list) - 1 - i]
        list[len(list) - 1 - i] = max(copy)
        list[indexOfMax] = temp

        copy.remove(max(copy))



def sort():
    lineInput = input("Enter ten integers: ").strip()
    numbers = [int(x) for x in lineInput.split()]

    selectionSort(numbers)

    print("The sorted numbers are:", end = " ")
    for i in numbers:
        print(i, end = " ")

    print()


def main():
    print([1, 1, 4, 4] == [1, 1, 4, 4])


main()
