'''
File name : countfib.py
Prints the number of calls of a recursive Fibonacci function with problem
sizes that double.
'''

def fib(n):
	#  count the number of calls of the Fibonacci function.
	global counter
	counter += 1
	if n<3:
		return 1
	else:
		return fib(n-1) + fib(n-2)

problemSize = 2
print("%12s%15s" % ("Problem Size", "Cells"))
for count in range(5):
	#counter = Counter()
	counter = 0
	fib(problemSize)
	print("%12s%15s" % (problemSize,counter))
	problemSize *= 2
