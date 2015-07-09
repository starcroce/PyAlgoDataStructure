# basic binary search, search for a num in sorted array
def binary_search_1(nums, target):
    start, end = 0, len(nums)-1
    while start + 1 < end:
        mid = start + (end - start) / 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid
        elif nums[mid] > target:
            end =  mid

    if nums[start] == target:
        return start
    elif nums[end] == target:
        return end
    else:
        return -1


# search for the first pos in duplicated elements array
# search for the last pos is the same, just change the first if to start=mid and compare nums[end] first
def binary_search_2(nums, target):
    start, end = 0, len(nums)-1
    while start + 1 < end:
        mid = start + (end - start) / 2
        if nums[mid] == target:
            end = mid
        elif nums[mid] < target:
            start = mid
        elif nums[mid] > target:
            end = mid

    if nums[start] == target:
        return start
    elif nums[end] == target:
        return end
    else:
        return -1


# search for the first num larger or equal to some number
# if search for the last num less or equal to some number, compare with nums[0] first, if nums[mid]==target, remove the first half
def binary_search_3(nums, target):
    if target > nums[-1]:
        return -1

    start, end = 0, len(nums)-1
    while start + 1 < end:
        mid = start + (end - start) / 2
        if nums[mid] == target:
            end = mid
        elif nums[mid] < target:
            start = mid
        elif nums[mid] > target:
            end = mid

    if nums[start] >= target:
        return start
    elif nums[end] >= target:
        return end


if __name__ == '__main__':
    target_1, target_2 = 5, 50

    nums = [i for i in range(10)]
    print binary_search_1(nums, target_1)
    print binary_search_1(nums, target_2)

    nums = [1, 5, 5, 7]
    print binary_search_2(nums, target_1)
    print binary_search_2(nums, target_2)

    nums = [6, 6, 7]
    print binary_search_3(nums, target_1)


