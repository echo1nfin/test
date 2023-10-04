from sys import setrecursionlimit as lim
from sys import set_int_max_str_digits as digits

lim(1000000)
digits(100000000)

# def fib(n, computed = {0: 0, 1: 1}):
# 	if n not in computed:
# 		computed[n] = fib(n-1, computed) + fib(n-2, computed)
# 	return computed[n]
# print(fib(400_000))

def fib(n):
	a, b = 0, 1
	for _ in range(n):
		a, b = b, a+b
	return a
print(fib(70))
# sp.urfu.ru
# 89197090793
# hawk321@mail.ru