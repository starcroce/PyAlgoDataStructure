# time O(n^2), space O(1)
def strstr_1(haystack, needle):
    i = 0
    while i < len(haystack)-len(needle)+1:
        if haystack[i] == needle[0]:
            j, k = 0, i
            while j < len(needle):
                if haystack[k] == needle[j]:
                    k += 1
                    j += 1
                else:
                    break
            if j == len(needle):
                return i
        i += 1
    return -1


# kmp algorithm, time O(n)
def strstr_2(haystack, needle):
    # create next table, next[0] = -1, next[1] = 0
    next = [0 for _ in range(len(needle))]
    next[0] = -1
    for i in range(2, len(needle)):
        prev = i - 1
        while prev != -1:
            if needle[i-1] == needle[next[prev]]:
                next[i] = next[prev] + 1
                break
            else:
                prev = next[prev]

    i, j = 0, 0
    while i < len(haystack) and j < len(needle):
        if haystack[i] == needle[j]:
            i += 1
            j += 1
        else:
            j = next[j]
            # means we have to compare from the beginning, reset j to 0 and i++
            if j == -1:
                j = 0
                i += 1

    if j == len(needle):
        return i - j
    else:
        return -1


if __name__ == '__main__':
    haystack = 'themississippi'
    needle_1 = 'issi'
    needle_2 = 'issii'

    print strstr_1(haystack, needle_1)
    print strstr_2(haystack, needle_1)

    print strstr_1(haystack, needle_2)
    print strstr_2(haystack, needle_2)
