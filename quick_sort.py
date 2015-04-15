import random


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) / 2]
    less, greater = [], []
    for num in arr:
        if num < pivot:
            less.append(num)
        elif num > pivot:
            greater.append(num)

    return quick_sort(less) + [pivot] + quick_sort(greater)


def main():
    arr = [x for x in range(10)]
    random.shuffle(arr)
    print arr

    arr = quick_sort(arr)
    print arr

if __name__ == '__main__':
    main()
