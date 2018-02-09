import sys

inv = int(sys.argv[1])


def perimeter(n):
    t1 = 0
    t2 = 1
    s = 1
    for i in range(n):
        temp = t1 + t2
        t1 = t2
        t2 = temp
        s = s + t2
    return s * 4


p = perimeter(inv)
print("Perimeter: " + str(p))
