# create suffix array, sort, get the longest common prefix between two continuous sub strings
# time O(nlogn), space O(n^2)
def longest_repeated_substring(str):
    suffix_arr = sorted([str[i:] for i in range(len(str))])
    res, max_len = set(), 0

    for i in range(len(suffix_arr) - 1):
        curr_len = 0
        for j in range(min(len(suffix_arr[i]), len(suffix_arr[i+1]))):
            if suffix_arr[i][j] == suffix_arr[i+1][j]:
                curr_len += 1
            else:
                break
        if curr_len > max_len:
            max_len = curr_len
            res.add(suffix_arr[i][:max_len])

    for s in list(res):
        if len(s) < max_len:
            res.remove(s)
    return max_len, res


if __name__ == '__main__':
    s = 'fdwaw4helloworldvcdv1c3xcv3xcz1sda21f2sd1ahelloworldgafgfa4564534321fadghelloworld'
    print longest_repeated_substring(s)
