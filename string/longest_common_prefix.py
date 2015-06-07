# n strings with average len m
# time O(mn), space O(1)
def longest_common_prefix(strs):
    res, max_len = '', min([len(s) for s in strs])
    for i in range(max_len):
        curr_char = strs[0][i]
        for j in range(1, len(strs)):
            if strs[j][i] != curr_char:
                return res
        res += curr_char
    return res


if __name__ == '__main__':
    strs = [
        'interspecies',
        'interstellar',
        'interstate'
    ]

    print longest_common_prefix(strs)
