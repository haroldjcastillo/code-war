from lib2to3.fixes import fix_throw


def answer(total_lambs):
    return stingy(total_lambs) - generous(total_lambs)


def generous(n):
    ttl = 1
    lst = 1
    a = 1
    v = [1]
    while n > 1:
        lst = lst * 2
        t = a + lst
        if t <= n:
            a = t
            ttl += 1
            v.append(lst)
        else:
            ttl, a, v = rule(lst / 4, lst / 2, (n - a), v, a, ttl)
            break
    print(v)
    print(n, a, (n - a))
    return ttl


def stingy(n):
    f = 1
    fp = 1
    a = 1
    ttl = 1
    v = [1]
    for i in range(2, n):
        if (f + a) > n:
            dif = n - a
            t = f - fp
            ttl, a, v = rule(t, fp, dif, v, a, ttl)
            break
        else:
            t = f
            f += fp
            fp = t
            a = fp + a
        v.append(fp)
        ttl += 1
    print(v)
    print(n, a, (n - a))
    return ttl


def rule(s1, s2, value, v, a, ttl):
    while value > 0:
        rsd = 0
        dbl = 2 * s2
        add = s1 + s2
        if add <= value <= dbl:
            a = a + value
            v.append(value)
            value = rsd
            ttl += 1
        elif value > dbl:
            rsd = value - dbl
            value = value - rsd
        else:
            break
    return ttl, a, v


print(answer(1953125))
print(answer(6561))
print(answer(1000))
print(answer(7776))
print(answer(40353607))
print(answer(125))
print(answer(59049))
print(answer(117649))
print(answer(1000000000))
print(answer(1))
print(answer(143))
print(answer(10))

import random

for i in range(1, 1):
    exp = random.randint(1, 9)
    base = random.randint(3, 10)
    n = base ** exp
    print(n, ' : ', answer(n))