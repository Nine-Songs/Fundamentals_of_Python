from numpy import *
import random
def mergesort(lyst):
	'''
	lyst:list being sorted
	copyBuffer temporary space needed during merge
	'''
	copyBuffer = zeros(len(lyst))
	mergeSortHelper(lyst,copyBuffer,0,len(lyst)-1)
	
def mergeSortHelper(lyst,copyBuffer,low,high):
	'''
	lyst      : list being sorted
	copyBuffer temp space needed during merge
	low,high  : bounds of sublist
	middle    : midpoint of sublist
	'''
	if low < high:
		middle = (low + high) // 2
		mergeSortHelper(lyst,copyBuffer,low,middle)
		mergeSortHelper(lyst,copyBuffer,middle + 1,high)
		merge(lyst,copyBuffer,low,middle,high)

def merge(lyst,copyBuffer,low,middle,high):
	
	'''
	Initialize i1 and i2 to the first items in each sublist
	'''
	i1 = low
	i2 = middle + 1
	
	for i in range(low,high + 1):
		if i1 > middle:
			copyBuffer[i] = lyst[i2] #First sublist exhausted
			i2 += 1
		elif i2 > high:
			copyBuffer[i] = lyst[i1] #Second sublist exhausted
			i1 += 1
		elif lyst[i1] < lyst[i2]:
			copyBuffer[i] = lyst[i1]
			i1 += 1                  #Item in first sublist <
		else:
			copyBuffer[i] = lyst[i2]
			i2 += 1                  #Item in second sublist <
	
	
	for i in range(low,high + 1):    #copy sorted items back to
		lyst[i] = copyBuffer[i]      #propre position in lyst
		
		
def main(size = 20,sort = mergesort):
	lyst = []
	for count in range(size):
		lyst.append(random.randint(1,size+1))
	print(lyst)
	sort(lyst)
	print(lyst)

if __name__ == "__main__":
	main()
