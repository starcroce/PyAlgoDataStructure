# time O(n^2), space O(1)
def longest_palindrome_1(s):
    if len(s) <= 1:
        return s
    res, start = 1, 0
    for i in range(len(s)-1):
        cur_len = longest_palindrome_1_helper(s, i, i)
        if cur_len > res:
            res = cur_len
            start = i - cur_len / 2
        cur_len = longest_palindrome_1_helper(s, i, i+1)
        if cur_len > res:
            res = cur_len
            start = i - (cur_len - 2) / 2
    return s[start : start+res]


def longest_palindrome_1_helper(s, pos1, pos2):
    while pos1 >= 0 and pos2 < len(s) and s[pos1] == s[pos2]:
        pos1 -= 1
        pos2 += 1
    return pos2 - pos1 - 1


# time O(n^2), space O(n^2)
# same question about lcs for s and reversed s
def longest_palindrome_2(s):
    revers_s = s[::-1]
    return longest_palindrome_2_helper(s, revers_s)


def longest_palindrome_2_helper(s1, s2):
    lcs = [[0 for _ in range(len(s2))] for _ in range(len(s1))]
    max_len, res = 0, ''

    for i in range(0, len(s1)):
        for j in range(0, len(s2)):
            if s1[i] == s2[j]:
                if i == 0 or j == 0:
                    lcs[i][j] = 1
                else:
                    lcs[i][j] = lcs[i-1][j-1] + 1

                if lcs[i][j] >= max_len:
                    max_len = lcs[i][j]
                    res = s1[i-max_len+1 : i+1]
    return res


# time O(n^3), space O(1)
def longest_palindrome_3(s):
    res, max_len = '', 0
    for i in range(len(s)):
        for j in range(1, len(s) + 1):
            tmp_s = s[i:j]
            if tmp_s == tmp_s[::-1] and len(tmp_s) > max_len:
                max_len = len(tmp_s)
                res = tmp_s
    return res


if __name__ == '__main__':
    s = '12212321'
    print longest_palindrome_1(s)
    print longest_palindrome_2(s)
    print longest_palindrome_3(s)
