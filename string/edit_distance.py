# the matrix size is (m+1) * (n+1)
# the numbers in first column and first row are from 0 to len(s1) and len(s2)
# 1. if s1[i-1] == s2[j-1], dist[i][j] = dist[i-1][j-1]
# 2. if s1[i-1] != s2[j-1], dist[i][j] = 1 + min(dist[i-1][j], dist[i][j-1], dist[i-1][j-1])
# time O(mn), space O(mn)
def edit_distance(s1, s2):
    # init distance matrix
    dist = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    for i in range(len(s1)+1):
        dist[i][0] = i
    for i in range(len(s2)+1):
        dist[0][i] = i

    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                dist[i][j] = dist[i-1][j-1]
            else:
                dist[i][j] = 1 + min(dist[i-1][j], dist[i][j-1], dist[i-1][j-1])

    return dist[-1][-1]


if __name__ == '__main__':
    s1 = 'sea'
    s2 = 'ate'

    print edit_distance(s1, s2)
