def max_sum_subarray(nums):
    currSum, currMin, currMax = 0, 0, 0-2**31
    for num in nums:
        currSum += num
        currMax = max(currMax, currSum-currMin)
        currMin = min(currMin, currSum)
    return currMax


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print max_sum_subarray(nums)
