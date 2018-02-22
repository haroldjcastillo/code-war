import numpy
import numpy as np
import matplotlib.pyplot as plt

board = numpy.arange(64).reshape((8, 8))
print(board)

am = np.zeros((64, 64))
print(am.shape)

def get_postion(pos):
    r = pos / 8
    c = (8 * r) - pos if pos < r else pos - (8 * r)
    return r, c


def get_childs(i):
    v = []
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
        v.append(board[ur2][lc1])
        am[i][board[ur2][lc1]] = 1
    if ur2 >= 0 and rc1 <= 7:
        v.append(board[ur2][rc1])
        am[i][board[ur2][rc1]] = 1
    if ur1 >= 0 and lc2 >= 0:
        v.append(board[ur1][lc2])
        am[i][board[ur1][lc2]] = 1
    if ur1 >= 0 and rc2 <= 7:
        v.append(board[ur1][rc2])
        am[i][board[ur1][rc2]] = 1
    if dr1 <= 7 and lc2 >= 0:
        v.append(board[dr1][lc2])
        am[i][board[dr1][lc2]] = 1
    if dr1 <= 7 and rc2 <= 7:
        v.append(board[dr1][rc2])
        am[i][board[dr1][rc2]] = 1
    if dr2 <= 7 and lc1 >= 0:
        v.append(board[dr2][lc1])
        am[i][board[dr2][lc1]] = 1
    if dr2 <= 7 and rc1 <= 7:
        v.append(board[dr2][rc1])
        am[i][board[dr2][rc1]] = 1
    return v


branches = []

for i in range(0, 64):
    branch = get_childs(i)
    branches.append(branch)
    """for j in range(len(branch)):
        plt.plot(i, branch[j], 'ro')"""
    # print i, branch

# print am
# print(get_postion(2))

# plt.axis([0, 63, 0, 63])
# plt.show()
