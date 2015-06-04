# lcs[i][j] means the max len of common substring that ends with s1[i] or s2[j]
# 1. if s1[i] == s2[j], lcs[i][j] = lcs[i-1][j-1] + 1
# 2. if s1[i] != s2[j], lcs[i][j] = 0
# time O(mn), space O(mn)
def longest_common_substring_dp(s1, s2):
    lcs = [[0 for _ in range(len(s2))] for _ in range(len(s1))]
    max_len, res_substr = 0, set()

    for i in range(0, len(s1)):
        for j in range(0, len(s2)):
            if s1[i] == s2[j]:
                if i == 0 or j == 0:
                    lcs[i][j] = 1
                else:
                    lcs[i][j] = lcs[i-1][j-1] + 1
                max_len = max(max_len, lcs[i][j])

                if lcs[i][j] >= max_len:
                    max_len = lcs[i][j]
                    res_substr.add(s1[i-max_len+1: i+1])

    for str in list(res_substr):
        if len(str) < max_len:
            res_substr.remove(str)
    return max_len, res_substr


# use suffix array, connect the two string with some special char like '#'
# the longest common substring is the longest duplicate substring of the new string
# when we compare the longest common prefix of sorted suffix array, make sure there is '#' in one of the two str
# that means that the two suffix substring come from different original string
# time O((m+n)log(m+n)), space O(mn)
def longest_common_substring_suffix_arr(s1, s2):
    new_str = s1 + '#' + s2
    suffix_arr = ['' for _ in range(len(new_str))]

    for i in range(len(new_str)):
        suffix_arr[i] = new_str[i:]
    suffix_arr.sort()

    max_len, res_substr = 0, set()
    for i in range(len(new_str) - 1):
        cur_len = compare_suffix_str(suffix_arr[i], suffix_arr[i+1])
        max_len = max(max_len, cur_len)

        if cur_len >= max_len:
            res_substr.add(suffix_arr[i][:max_len])

    for str in list(res_substr):
        if len(str) < max_len:
            res_substr.remove(str)
    return max_len, res_substr


def compare_suffix_str(s1, s2):
    res = 0
    if s1.find('#') == -1 and s2.find('#') == -1:
        return res

    for i in range(max(len(s1), len(s2))):
        if s1[i] == s2[i]:
            res += 1
        else:
            break
    return res


if __name__ == '__main__':
    s1 = 'I love programming all day and all night'
    s2 = 'If I have to write one more program, I will change majors'

    print longest_common_substring_dp(s1, s2)
    print longest_common_substring_suffix_arr(s1, s2)
