import random


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) / 2
    left, right = arr[0:mid], arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    res = []

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            res.append(left[0])
            left.pop(0)
        else:
            res.append(right[0])
            right.pop(0)

    res += left if len(left) > 0 else right
    return res


def main():
    arr = [x for x in range(10)]
    random.shuffle(arr)
    print arr

    arr = merge_sort(arr)
    print arr

if __name__ == '__main__':
    main()
