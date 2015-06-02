def longest_common_substring(s1, s2):
    lcs = [[0 for _ in range(len(s2))] for _ in range(len(s1))]
    max_len, res_substr = 0, set()
    for i in range(0, len(s1)):
        for j in range(0, len(s2)):
            if s1[i] == s2[j]:
                if i == 1 or j == 1:
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

if __name__ == '__main__':
    s1 = 'I love programming all day and all night'
    s2 = 'If I have to write one more program, I will change majors'
    print longest_common_substring(s1, s2)[0]
    print longest_common_substring(s1, s2)[1]
