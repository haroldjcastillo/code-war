from fractions import Fraction


def swap(m, i, j):
    n = []
    s = len(m)

    if s != len(m[0]):
        raise Exception("It's non-square matrix")
    if i == j:
        return m

    for r in range(s):
        rw = []
        twr = m[r]
        if r == i:
            twr = m[j]
        if r == j:
            twr = m[i]
        for c in range(s):
            tmp = twr[c]
            if c == i:
                tmp = twr[j]
            if c == j:
                tmp = twr[i]
            rw.append(tmp)
        n.append(rw)
    return n


def sort(m):
    size = len(m)
    j = -1
    for r in range(size):
        s = sum(m[r])
        if s == 0:
            j = r
        elif s != 0 and j > -1:
            n = swap(m, r, j)
            return sort(n)
    return m


def normalize(m, use_fractions=False):
    n = []
    for r in range(len(m)):
        cols = len(m[r])
        s = sum(m[r])
        rw = []
        if s == 0:
            rw = m[r]
        else:
            for c in range(cols):
                if use_fractions:
                    rw.append(Fraction(m[r][c], s))
                else:
                    rw.append(float(m[r][c]) / s)
        n.append(rw)
    return n


def get_absorbing_states_count(m):
    if len(m) == 0:
        raise Exception("Empty matrix")

    for r in range(len(m)):
        for c in range(len(m[r])):
            if m[r][c] != 0:
                break
        else:
            return r
    raise Exception("Invalid matrix")


def get_transitions(m):
    t = get_absorbing_states_count(m)

    if t == 0:
        raise Exception("Invalid absorbing state.")

    q = []
    for r in range(t):
        tq = []
        for c in range(t):
            tq.append(m[r][c])
        q.append(tq)
    if q is None:
        raise Exception("Invalid matrix")

    r = []
    for i in range(t):
        tr = []
        for j in range(t, len(m[i])):
            tr.append(m[i][j])
        r.append(tr)
    if r is None:
        raise Exception("Invalid matrix")
    return q, r


def identity(s):
    i = []
    for r in range(s):
        rw = []
        for j in range(s):
            rw.append(int(r == j))
        i.append(rw)
    return i


def subtract(i, q):
    if len(i) != len(i[0]) or len(q) != len(q[0]):
        raise Exception("non-square matrices")

    if len(i) != len(q) or len(i[0]) != len(q[0]):
        raise Exception("Cannot subtract matrices of different sizes")

    s = []
    for r in range(len(i)):
        rw = []
        for c in range(len(i[r])):
            rw.append(i[r][c] - q[r][c])
        s.append(rw)
    return s


def minor(m, i, j):
    return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]


def determinant(m):
    # base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    d = 0
    for c in range(len(m)):
        d += ((-1) ** c) * m[0][c] * determinant(minor(m, 0, c))

    return d


def transpose(m):
    t = []
    for r in range(len(m)):
        tRow = []
        for c in range(len(m[r])):
            if c == r:
                tRow.append(m[r][c])
            else:
                tRow.append(m[c][r])
        t.append(tRow)
    return t


def inverse(m):
    d = determinant(m)

    if d == 0:
        raise Exception("Invalid matrix determinant")

    if len(m) == 2:
        return [[m[1][1] / d, -1 * m[0][1] / d],
                [-1 * m[1][0] / d, m[0][0] / d]]

    cfs = []
    for r in range(len(m)):
        cr = []
        for c in range(len(m)):
            minor = minor(m, r, c)
            cr.append(((-1) ** (r + c)) * determinant(minor))
        cfs.append(cr)
    cfs = transpose(cfs)
    for r in range(len(cfs)):
        for c in range(len(cfs)):
            cfs[r][c] = cfs[r][c] / d
    return cfs


def multiply(a, b):
    if a == [] or b == []:
        raise Exception("Empty matrix")

    if len(a[0]) != len(b):
        raise Exception("Invalid size matrix")

    m = []
    for r in range(len(a)):
        rw = []
        for c in range(len(b[0])):
            s = 0
            for i in range(len(a[0])):
                s += a[r][i] * b[i][c]
            rw.append(s)
        m.append(rw)
    return m


def get_common(a, b):
    g = b
    if a > b:
        g = a
    while True:
        if g % a == 0 and g % b == 0:
            c = g
            break
        g += 1
    return c


def to_lcm(p):
    ret = []

    c = reduce(lambda x, y: get_common(x, y), [f.denominator for f in p])
    for f in p:
        if f.denominator != c:
            ret.append(Fraction(c / f.denominator * f.numerator, c))
        else:
            ret.append(Fraction(f.numerator, c))
    return ret


def answer(m):
    m = sort(m)
    n = normalize(m, use_fractions=True)
    (q, r) = get_transitions(n)
    i = identity(len(q))
    s = subtract(i, q)
    v = inverse(s)
    b = to_lcm(multiply(v, r)[0])

    return b


mx = [[0, 1, 0, 0, 0, 1],  # s0
      [4, 0, 0, 3, 2, 0],  # s1
      [0, 0, 0, 0, 0, 0],  # s2
      [0, 0, 0, 0, 0, 0],  # s3
      [0, 0, 0, 0, 0, 0],  # s4
      [0, 0, 0, 0, 0, 0]]  # s5

print answer(mx)
