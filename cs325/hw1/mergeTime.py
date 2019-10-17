# AUTHOR: Written by Junhyeok Jeong (jeongju@oregonstate.edu)
# ID: 933196042
# CLASS: CS325 - 400 (2019 Fall)
# ASSIGNMENT: Homework 1

import string
import numpy
import random
import time

def mergesort(arr):
	if len(arr) > 1:
		#finding mid and then divide into left and right of the input array
		mid = len(arr)//2
		left = arr[:mid]
		right = arr[mid:]
		
		mergesort(left)
		mergesort(right)

		i = j = k = 0
		#copy integers to temporary arrays
		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				arr[k] = left[i]
				i = i + 1
			else:
				arr[k] = right[j]
				j = j + 1
			k = k + 1

		#checking element was in the left array
		while i < len(left):
			arr[k] = left[i]
			i = i + 1
			k = k + 1
		while j < len(right):
			arr[k] = right[j]
			j = j + 1
			k = k + 1


n = 0

#creat an array with n (the number of elements)
for j in range(10):
	array = []
	n = n+ 20000 

#set array element's value randomly
	for i in range(0, n):
		array.append(random.randint(0,10000))


#measure start time
	start_time = time.time()

#merge sort
	mergesort(array)

	print("array size n: {}, running time: {} seconds ".format(n, time.time() - start_time))	
