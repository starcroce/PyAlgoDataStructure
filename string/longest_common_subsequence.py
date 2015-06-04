# lcs[i][j] means the max len of common sub sequence that ends with s1[i] and s2[j]
# 1. if s1[i] == s2[j], lcs[i][j] = lcs[i-1][j-1] + 1
# 1.1. if i == 0 or j == 0, lcs[i][j] = 0
# 2. if s1[i] != s2[j], lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
# time O(mn), space O(mn)
def longest_common_subseq_dp(s1, s2):
    lcs = [[0 for _ in range(len(s2))] for _ in range(len(s1))]

    for i in range(len(s1)):
        seq = ''
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                seq += s1[i]
                if i == 0 or j == 0:
                    lcs[i][j] = 1
                else:
                    lcs[i][j] = lcs[i-1][j-1] + 1
            else:
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

    seq, res_seq = '', set()
    get_lc_seq(s1, s2, lcs, len(s1)-1, len(s2)-1, seq, res_seq)

    return lcs[-1][-1], res_seq


# trace back to get all the common sub sequence using dfs
# need to reverse the final seq since we start from bottom right
def get_lc_seq(s1, s2, lcs, i, j, seq, res_seq):
    while i >= 0 and j >= 0:
        if s1[i] == s2[j]:
            seq += s1[i]
            i -= 1
            j -= 1
        else:
            if lcs[i-1][j] > lcs[i][j-1]:
                i -= 1
            elif lcs[i-1][j] < lcs[i][j-1]:
                j -= 1
            else:
                get_lc_seq(s1, s2, lcs, i-1, j, seq, res_seq)
                get_lc_seq(s1, s2, lcs, i, j-1, seq, res_seq)
                return
    res_seq.add(seq[::-1])


if __name__ == '__main__':
    s1 = 'BDCABA'
    s2 = 'ABCBDAB'

    print longest_common_subseq_dp(s1, s2)
