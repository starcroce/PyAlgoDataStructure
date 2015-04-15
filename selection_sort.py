import random


def selection_sort(arr):
    if len(arr) <= 1:
        return arr

    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


def main():
    arr = [x for x in range(10)]
    random.shuffle(arr)
    print arr

    arr = selection_sort(arr)
    print arr

if __name__ == '__main__':
    main()
