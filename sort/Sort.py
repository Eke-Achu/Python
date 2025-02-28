def is_sorted(lst):
    copy = [] + lst

    copy.sort()

    return copy == lst


def bubble_sort(lst):
    for i in range(len(lst)):
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]

def main():
    lst = [int(x) for x in input("Enter list: ").strip().split()]

    # print("The list is", "not" if not is_sorted(lst) else "already", "sorted")

    bubble_sort(lst)
    print(lst)

main()
