import sys

inv = int(sys.argv[1])


def decompose(n):
    x = 0
    _n = n = n ** 2
    v2 = []
    v = []
    while x != _n:
        if n == 1 and x < _n and len(v) == 1:
            return None
        elif n == 1 and x < _n:
            n_0 = v[0]
            x_0 = v2[0]
            n = v[0] ** 2
            x = v2[0]
            v.clear()
            v2.clear()
            v.append(n_0)
            v2.append(x_0)
        else:
            n = perfect_sqr(n)
            dif = n + x
            if dif <= _n:
                x = dif
                v2.append(x)
                v.append(int(n ** 0.5))
    v = v[::-1]
    return v


def perfect_sqr(n):
    sqr = n ** 0.5
    if n % sqr == 0:
        return (sqr - 1) ** 2


# for i in range(1, len(sys.argv)):
#     print(decompose(int(sys.argv[i])))

print(decompose(44))
