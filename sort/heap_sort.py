import random


def heap_sort(arr):
    if len(arr) <= 1:
        return arr

    for i in range(len(arr) / 2 - 1, -1, -1):
        arr = shift_down(arr, i, len(arr) - 1)

    for i in xrange(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        arr = shift_down(arr, 0, i - 1)

    return arr


def shift_down(arr, start, end):
    root = start
    while True:
        child = root * 2 + 1
        if child > end:
            break
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1
        if arr[root] < arr[child]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child
        else:
            break
    return arr


def main():
    arr = [x for x in range(10)]
    random.shuffle(arr)
    print arr

    arr = heap_sort(arr)
    print arr


if __name__ == '__main__':
    main()
