def insertionSort(lyst):
	i = 1
	while i < len(lyst):
		itemToInsert = lyst[i]
		j = i - 1
		while j >= 0:
			if itemToInsert < lyst[j]:
				lyst[j+1] = lyst[j]
				j -= 1
			else:
				break
		lyst[j+1] = itemToInsert  #where we want to insert
		i += 1                    #begin the next cycle

lystA = [5,4,23,6,34]
print(lystA)
insertionSort(lystA)
print(lystA)
