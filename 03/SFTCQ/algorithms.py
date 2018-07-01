'''
File : algorithms.py
Algorithms configured for profiling.
'''
from numpy import *
import random

########################################################################
###########################selectionSort################################
def selectionSort(lyst,profiler):
	i = 0
	while i < len(lyst) - 1:
		minIndex = i
		j = i + 1
		while j < len(lyst):
			profiler.comparison()  #count
			if lyst[j] < lyst[minIndex]:
				minIndex = j
			j += 1
		if minIndex != i:
			swap(lyst, minIndex ,i,profiler)
		i += 1
########################################################################
########################################################################



########################################################################
#############################quickSort##################################
def quickSort(lyst,profiler):
	quicksortHelper(lyst,0,len(lyst)-1,profiler)
	
def quicksortHelper(lyst,left,right,profiler):
	if left < right:
		pivotLocation = partition(lyst,left,right,profiler)
		quicksortHelper(lyst,left,pivotLocation-1,profiler)
		quicksortHelper(lyst,pivotLocation+1,right,profiler)
def partition(lyst,left,right,profiler):
	#Find the pivot and exchange it with the last item
	middle = (left + right) // 2
	piovt = lyst[middle]
	lyst[middle] = lyst[right]
	lyst[right] = piovt
	#Set boundary point to first position
	boundary = left
	#Move items less than pivot to the left
	for index in range(left,right):
		profiler.comparison()
		if lyst[index] < piovt:
			swap(lyst,index,boundary,profiler)
			boundary += 1
	#Exchange the pivot item and the boundary item
	swap(lyst,right,boundary,profiler)
	return boundary

########################################################################
########################################################################





########################################################################
########################################################################	
def mergeSort(lyst,profiler):
	'''
	lyst:list being sorted
	copyBuffer temporary space needed during merge
	'''
	copyBuffer = zeros(len(lyst))
	mergeSortHelper(lyst,copyBuffer,0,len(lyst)-1,profiler)
	
def mergeSortHelper(lyst,copyBuffer,low,high,profiler):
	'''
	lyst      : list being sorted
	copyBuffer temp space needed during merge
	low,high  : bounds of sublist
	middle    : midpoint of sublist
	'''
	if low < high:
		middle = (low + high) // 2
		mergeSortHelper(lyst,copyBuffer,low,middle,profiler)
		mergeSortHelper(lyst,copyBuffer,middle + 1,high,profiler)
		merge(lyst,copyBuffer,low,middle,high,profiler)

def merge(lyst,copyBuffer,low,middle,high,profiler):
	
	'''
	Initialize i1 and i2 to the first items in each sublist
	'''
	i1 = low
	i2 = middle + 1
	
	for i in range(low,high + 1):
		profiler.comparison()
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
		profiler.comparison()
		lyst[i] = copyBuffer[i]      #propre position in lyst
		
########################################################################
########################################################################




########################################################################
########################################################################
def bubbleSort(lyst,profiler):
	n = len(lyst)
	while n > 1:
		profiler.comparison()
		i = 1
		while i < n:
			profiler.comparison()
			if lyst[i] < lyst[i-1]:
				swap(lyst,i,i-1,profiler)
			i += 1
		n -= 1
########################################################################
########################################################################
def insertionSort(lyst,profiler):
	i = 1
	while i < len(lyst):
		profiler.comparison()
		itemToInsert = lyst[i]
		j = i - 1
		while j >= 0:
			profiler.comparison()
			if itemToInsert < lyst[j]:
				lyst[j+1] = lyst[j]
				j -= 1
			else:
				break
		lyst[j+1] = itemToInsert  #where we want to insert
		i += 1                    #begin the next cycle

########################################################################
########################################################################



########################################################################
########################################################################
def swap(lyst,i,j,profiler):
	'''
	Exchange the elements at postions i and j.
	'''
	profiler.exchange()
	temp = lyst[i]
	lyst[i] = lyst[j]
	lyst[j] = temp
########################################################################
########################################################################	
# Testing code can go here , optionally
