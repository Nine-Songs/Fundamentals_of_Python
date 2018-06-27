'''
Returns the index of the minimun item
O(n)
'''

def indexOfMin(lyst):
	minIndex = 0  #the index of the minimum item is 0
	currentIndex = 1  
	while currentIndex < len(lyst):
		if lyst[minIndex] > lyst[currentIndex]:
			minIndex = currentIndex
		currentIndex += 1
	return minIndex
