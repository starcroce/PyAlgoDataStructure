import random


def bubble_sort(arr):
    if len(arr) <= 1:
        return arr

    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


def main():
    arr = [x for x in range(10)]
    random.shuffle(arr)
    print arr

    arr = bubble_sort(arr)
    print arr


if __name__ == '__main__':
    main()
