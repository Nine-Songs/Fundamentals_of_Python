'''
Two-fork search function with sequence table
'''
def binarySearch(target,lyst):
	left = 0
	right = len(lyst)-1
	print("%s%12s%12s" % ("left","midpoint","right"))
	while left <= right :
		midpoint = (left + right) // 2
		print("%s%12s%12s" % (lyst[left],lyst[midpoint],lyst[right]))
		if lyst[midpoint] == target:
			return midpoint
		elif lyst[midpoint] < target:
			left = midpoint + 1
		elif lyst[midpoint] > target:
			right = midpoint - 1
	return -1

targetList = ['20','44','48','55','62','66','74','88','93','99']
postion = binarySearch('48',targetList)
print("the postion is: ")
if postion == -1:
	print("not found")

else:
	print(postion)
