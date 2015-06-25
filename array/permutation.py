def permutation_1(nums):
    res, visited = [], [False for _ in range(len(nums))]
    sol = []
    permutation_1_helper(nums, 0, visited, sol, res)
    return res


def permutation_1_helper(nums, start, visited, sol, res):
    if len(sol) == len(nums):
        res.append(sol)
        return

    for i in range(len(nums)):
        if visited[i] is False:
            sol.append(nums[i])
            visited[i] = True
            permutation_1_helper(nums, i+1, visited, sol, res)
            visited[i] = False
            sol = sol[:-1]


# [a] -> [ba, ab] -> [cba, bca, bac, cab, acb, abc]
# replace the res list after inserting a new char
def permutation_2(nums):
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


if __name__ == '__main__':
    s = [1, 2, 3, 4]

    print permutation_1(s)
    print permutation_2(s)
