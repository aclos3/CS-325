# AUTHOR: Written by Junhyeok Jeong (jeongju@oregonstate.edu)
# ID: 933196042
# CLASS: CS325 - 400 (2019 Fall)
# ASSIGNMENT: Homework 1

import string
import numpy
import random
import time

n = 0
#create an array with n elements
for i in range(10):
	array =[]
	n = n+ 1000

#set element's value randomly
	for i in range(0, n):
		array.append(random.randint(0,10000))

#measure time
	start_time = time.time()

#insertion sort process with a key
	for i in range(0, n):
		insertion_key = array[i]
		j = i - 1
			
		while j >= 0 and insertion_key < array[j]:
			array[j+1] = array[j]
			j = j - 1
		array[j+1] = insertion_key

	print("array size n: {}, running time: {} seconds ".format(n, time.time() - start_time))	
