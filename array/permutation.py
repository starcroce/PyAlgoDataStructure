def permutation_1(nums):
    res, sol = [], []
    visited = [False for _ in range(len(nums))]
    permutation_1_helper(nums, visited, sol, res)
    return res


def permutation_1_helper(nums, visited, sol, res):
    if len(sol) == len(nums):
        # if it is res.append(sol), it only append an empty list
        # WTF!!!!!!
        res.append(sol[:])
        return

    for i in range(len(nums)):
        if visited[i] is False:
            visited[i] = True
            sol.append(nums[i])
            permutation_1_helper(nums, visited, sol, res)
            sol.pop()
            visited[i] = False


# [a] -> [ba, ab] -> [cba, bca, bac, cab, acb, abc]
# replace the res list after inserting a new char
def permutation_2(nums):
    # use another stack to make sure that nums won't be affected during the function
    stack = list(nums)
    res = [[stack.pop()]]
    while len(stack) > 0:
        tmp = stack.pop()
        new_res = []
        for sol in res:
            for i in range(len(sol)+1):
                new_res.append(sol[:i] + [tmp] + sol[i:])
        res = new_res
    return res


def permutation_2_unique(nums):
    res = permutation_2(nums)
    res = set([tuple(item) for item in res])
    res = [list(item) for item in res]
    return res


if __name__ == '__main__':
    nums = [1, 2, 3, 3]

    print permutation_1(nums)
    print permutation_2(nums)
    print permutation_2_unique(nums)
