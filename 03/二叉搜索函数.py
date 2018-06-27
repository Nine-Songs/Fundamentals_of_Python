'''
Two-fork search function with sequence table
'''
def binarySearch(target,lyst):
	left = 0
	right = len(lyst)-1
	while left <= right :
		midpoint = (left + right) // 2
		if lyst[midpoint] == target:
			return midpoint
		elif lyst[midpoint] < target:
			left = midpoint + 1
		elif lyst[midpoint] > target:
			right = midpoint - 1
	return -1
