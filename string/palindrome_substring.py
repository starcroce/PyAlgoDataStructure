def is_palindrome(s):
    return s == s[::-1]


# time O(n^2), space O(1)
def longest_palindrome(s):
    if len(s) <= 1:
        return s
    res, start = 1, 0
    for i in range(len(s)-1):
        cur_len = longest_palindrome_helper(s, i, i)
        if cur_len > res:
            res = cur_len
            start = i - cur_len / 2
        cur_len = longest_palindrome_helper(s, i, i+1)
        if cur_len > res:
            res = cur_len
            start = i - (cur_len - 2) / 2
    return s[start: start+res]


def longest_palindrome_helper(s, pos1, pos2):
    while pos1 >= 0 and pos2 < len(s) and s[pos1] == s[pos2]:
        pos1 -= 1
        pos2 += 1
    return pos2 - pos1 - 1


if __name__ == '__main__':
    s1, s2, s3 = 'aba', 'abba', 'abc'
    print is_palindrome(s1), is_palindrome(s2), is_palindrome(s3)

    s4 = '12212321'
    print longest_palindrome(s4)
