def subsets_1(nums):
    res, sol, pos = [], [], 0
    subsets_1_helper(nums, pos, sol, res)
    return res


def subsets_1_helper(nums, pos, sol, res):
    res.append(sol[:])
    for i in range(pos, len(nums)):
        sol.append(nums[i])
        subsets_1_helper(nums, i+1, sol, res)
        sol.pop()


def subsets_1_unique(nums):
    res, sol, pos = [], [], 0
    subsets_1_unique_helper(sorted(nums), pos, sol, res)
    return res


def subsets_1_unique_helper(nums, pos, sol, res):
    res.append(sol[:])
    for i in range(pos, len(nums)):
        if i > pos and nums[i-1] == nums[i]:
            continue
        sol.append(nums[i])
        subsets_1_unique_helper(nums, i+1, sol, res)
        sol.pop()


# for each index, 1 means choosing this number, 0 means not choosing this number
# so all subsets are equal to 0...0 to 1...1
def subsets_2(nums):
    res = []
    for i in range(2 ** len(nums)):
        sol = []
        for j in range(len(nums)):
            if i & (2 ** j):
                sol.append(nums[j])
        res.append(sol)
    return res


def subsets_2_unique(nums):
    res = set()
    for i in range(2 ** len(nums)):
        sol = []
        for j in range(len(nums)):
            if i & (2 ** j):
                sol.append(nums[j])
        res.add(tuple(sol))
    return [list(item) for item in res]


if __name__ == '__main__':
    nums = [1, 2, 3, 3]

    print subsets_1(nums)
    print subsets_2(nums)

    print subsets_1_unique(nums)
    print subsets_2_unique(nums)
