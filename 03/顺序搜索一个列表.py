'''
Returns the position of the target item if found , or -1 otherwise
'''
def sequentialSearch(target,lyst):
	position = 0
	while position < len(lyst):
		if lyst[position] == target:
			return position
		position += 1
	return -1
