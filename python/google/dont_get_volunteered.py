c = 0
board = [[0] * 8 for u in range(8)]
for x in range(0, 8):
    for y in range(0, 8):
        board[x][y] = c
        c += 1

am = [[float('inf')] * 64 for q in range(64)]


def answer(src, dest):
    if src == dest:
        return 1

    for i in range(0, 64):
        add_adjacency_matrix(i)
    floyd_warshall()

    return am[src][dest]


def get_postion(pos):
    r = pos / 8
    c = (8 * r) - pos if pos < r else pos - (8 * r)
    return r, c


def add_adjacency_matrix(i):
    r, c = get_postion(i)
    dr2 = r + 2
    ur2 = r - 2
    lc1 = c - 1
    rc1 = c + 1
    dr1 = r + 1
    ur1 = r - 1
    lc2 = c - 2
    rc2 = c + 2

    if ur2 >= 0 and lc1 >= 0:
        am[i][board[ur2][lc1]] = 1
    if ur2 >= 0 and rc1 <= 7:
        am[i][board[ur2][rc1]] = 1
    if ur1 >= 0 and lc2 >= 0:
        am[i][board[ur1][lc2]] = 1
    if ur1 >= 0 and rc2 <= 7:
        am[i][board[ur1][rc2]] = 1
    if dr1 <= 7 and lc2 >= 0:
        am[i][board[dr1][lc2]] = 1
    if dr1 <= 7 and rc2 <= 7:
        am[i][board[dr1][rc2]] = 1
    if dr2 <= 7 and lc1 >= 0:
        am[i][board[dr2][lc1]] = 1
    if dr2 <= 7 and rc1 <= 7:
        am[i][board[dr2][rc1]] = 1


def floyd_warshall():
    for k in range(0, 64):
        for i in range(0, 64):
            for j in range(0, 64):
                if am[i][k] + am[k][j] < am[i][j]:
                    am[i][j] = am[i][k] + am[k][j]


print get_postion(28)
print get_postion(55)

print 0, 0, answer(0, 0)
print 0, 1, answer(0, 1)
print 19, 36, answer(19, 36)
print 6, 44, answer(6, 44)
print 0, 63, answer(0, 63)
print 0, 32, answer(0, 32)
print 56, 7, answer(56, 7)
print 56, 56, answer(56, 56)
