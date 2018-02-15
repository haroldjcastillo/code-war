import sys

inv = int(sys.argv[1])

def answer(area):

	import math

	ans = []

	while area >= 1:
		s = math.sqrt(area)
		l = s - (s % 1)
		r = math.pow(l, 2)
		area = area - r
		ans.append(r)

	return ans


print(answer(inv))
