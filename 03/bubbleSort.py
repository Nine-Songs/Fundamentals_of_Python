def swap(lyst,i,j):
	'''
	Exchange the items in postion i and postion j.
	'''
	temp = lyst[i]
	lyst[i] = lyst[j]
	lyst[j] = temp

def bubbleSort(lyst):
	n = len(lyst)
	while n > 1:
		i = 1
		while i < n:
			if lyst[i] < lyst[i-1]:
				swap(lyst,i,i-1)
			i += 1
		n -= 1
lystA = [5,4,23,6,34]
print(lystA)
bubbleSort(lystA)
print(lystA)
