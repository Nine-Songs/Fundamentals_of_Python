
def fib(n):
	'''
	Count the number of iterations in the Fibonacci function.
	'''
	global counter
	sum = 1
	first = 1
	second = 1
	count = 3
	while count <= n:
		counter += 1
		sum = first + second
		first = second
		second = sum
		count += 1
	return sum

problemSize = 2
print("%12s%15s" % ("Problem Size", "Cells"))
for count in range(5):
	counter = 0
	fib(problemSize)
	print("%12s%15s" % (problemSize,counter))
	problemSize *= 2

