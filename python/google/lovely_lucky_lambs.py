def answer(total_lambs):
    return stingy(total_lambs) - generous(total_lambs)


def generous(n):
    ttl = 1
    lst = 1
    a = 0
    while True:
        lst = lst * 2
        a = a + lst
        if a <= n:
            ttl += 1
        else:
            break
    return ttl


def stingy(n):
    if n <= 1:
        return n
    f = 1
    fp = 1
    a = 1
    ttl = 1
    for i in range(2, n):
        t = f
        f += fp
        fp = t
        a = fp + a
        if a > n:
            break
        ttl += 1
    return ttl


print(answer(10) == 1)
print(answer(143) == 3)