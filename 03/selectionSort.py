def swap(lyst,i,j):
	'''
	Exchanges the items at postion i and j.
	'''
	temp = lyst[i]
	lyst[i] = lyst[j]
	lyst[j] = temp

#  
#  name: selectionSort
#  @param a lyst
#  @return none
#  
def selectionSort(lyst):
	i = 0
	while i < len(lyst) - 1:
		minIndex = i
		j = i + 1
		while j < len(lyst):
			if lyst[j] < lyst[minIndex]:  #start a search to find min number
				print(lyst[minIndex])     #just debug
				minIndex = j
				
			j += 1
		if minIndex != i:
			swap(lyst,minIndex,i)
		i += 1
			
lystA = [3,34,32,45,98,21]
print(lystA)
selectionSort(lystA)
print(lystA)
			
