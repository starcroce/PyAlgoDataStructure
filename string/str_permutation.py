def permutation_1(s):
    res, visited = [], [False for _ in range(len(s))]
    sol = ''
    permutation_1_helper(s, 0, visited, sol, res)
    return res


def permutation_1_helper(s, start, visited, sol, res):
    if len(sol) == len(s):
        res.append(sol)
        return

    for i in range(len(s)):
        if visited[i] is False:
            sol += s[i]
            visited[i] = True
            permutation_1_helper(s, i+1, visited, sol, res)
            visited[i] = False
            sol = sol[:-1]


# [a] -> [ba, ab] -> [cba, bca, bac, cab, acb, abc]
# replace the res list after inserting a new char
def permutation_2(s):
    stack = list(s)
    res = [stack.pop()]
    while len(stack) > 0:
        tmp = stack.pop()
        new_res = []
        for c in res:
            for i in range(len(c)+1):
                new_res.append(c[:i] + tmp + c[i:])
        res = new_res
    return res


if __name__ == '__main__':
    s = 'abcd'

    print permutation_1(s)
    print permutation_2(s)
