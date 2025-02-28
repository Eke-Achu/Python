def selection_sort(lst):

    for i in range(len(lst) - 1):
        current_min = min(lst[i : ]) 
        current_min_index = lst[i : ].index(current_min)

        lst[i], lst[i + current_min_index] = current_min, lst[i]

def main():
    lst = [20, 10, 4, 9, 5, 2, 50, 1, 3, 0, 4, 4, 9, 46, -2]
    selection_sort(lst)
    print(lst)

main()
