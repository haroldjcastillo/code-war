def answer():
    pass


def sort(m):
    size = len(m)

    for r in reversed(range(size)):
        s = 0
        for c in range(size):
            s += m[r][c]
        if s == 0:
            m.append(m[r])
            del m[r]
    return m


m = [[1,1,1,1],  #s0
     [0, 0, 0, 0],  # s1
     [0, 0, 0, 0],  # s2
     [1, 2, 3, 4]]  # s3

print sort(m)