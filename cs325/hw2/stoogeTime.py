# AUTHOR: Written by Junhyeok Jeong (jeongju@oregonstate.edu)
# ID: 933196042
# CLASS: CS325 - 400 (2019 Fall)
# ASSIGNMENT: Homework 2

import string
import numpy
import random
import time

def stoogesort(array, first, last):
	if  last <= first:
		return
	
#step 1: if first element is bigger than last element, then swap
	if int(array[first]) > int(array[last]):
		temp = array[last]
		array[last] = array[first]
		array[first] = temp

#step 2: if there are 3 or more elements in the array, then
	if last - first + 1 >= 3:
		one_third = int(((last - first + 1) / 3))

#recursively call stooge sort with the initial 2/3 of the array
		stoogesort(array, first, (last - one_third))
#recursively call stooge sort with the last 2/3 of the array
		stoogesort(array, first + one_third, last)
#recursively call stooge sort with the initial 2/3 of the array again
		stoogesort(array, first, (last - one_third))
	

n = 0

#creat an array with n (the number of elements)
for j in range(10):
	array = []
	n = n+ 50 

#set array element's value randomly
	for i in range(0, n):
		array.append(random.randint(0,10000))


#measure start time
	start_time = time.time()

#stooge sort
	stoogesort(array, 0, n-1)

	print("array size n: {}, running time: {} seconds ".format(n, time.time() - start_time))	
