import random


def insertion_sort(arr):
    if len(arr) <= 1:
        return arr

    for i in range(1, len(arr)):
        tmp, j = arr[i], i - 1
        while j >= 0 and tmp < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = tmp

    return arr


def main():
    arr = [x for x in range(10)]
    random.shuffle(arr)
    print arr

    arr = insertion_sort(arr)
    print arr


if __name__ == '__main__':
    main()
