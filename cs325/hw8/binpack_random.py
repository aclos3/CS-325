# AUTHOR: Written by Junhyeok Jeong (jeongju@oregonstate.edu)
# ID: 933196042
# CLASS: CS325 - 400 (2019 Fall)
# ASSIGNMENT: Homework 8

import sys
import string
import numpy
import math
import collections
import time
import random

def merge_sort(ar):
	if len(ar) > 1:
		mid = len(ar) // 2 
		left = ar[:mid]
		right = ar[mid:]

		merge_sort(left)
		merge_sort(right)

		i = j = k = 0

		while i < len(left) and j < len(right):
			if left[i] > right[j]:
				ar[k] = left[i]
				i += 1
			else:
				ar[k] = right[j]
				j += 1
			k += 1

		while i < len(left):
			ar[k] = left[i]
			k += 1
			i += 1
		while j < len(right):
			ar[k] = right[j]
			k += 1
			j += 1

def first_fit(bin_capacity, item_weights):
	#initialize the bin_ar with first default bin
	bin_ar = [bin_capacity]

	#outer loop is for looping the item list (item_weights)
	for i in range(len(item_weights)):
		j = 0
		#innner loop is for checking space of bins and then deduction
		while j < len(bin_ar):
			if bin_ar[j] - item_weights[i] >= 0:
				bin_ar[j] = bin_ar[j] - item_weights[i]
				break
		
			#if there is no enough space, then create new bin
			else:
				if len(bin_ar) - 1 == j:
					bin_ar.append(bin_capacity)
			j += 1
				
	return len(bin_ar)

def first_fit_drecreasing(bin_capacity, item_weights):
	#set temp sorted item array
	sorted_items = []
	for i in item_weights:
		sorted_items.append(i)
	
	#merge sort O(nlogn)
	merge_sort(sorted_items)

	#use the first fit for sorted array
	return first_fit(bin_capacity, sorted_items)

def best_fit(bin_capacity, item_weights):
	#initialize bin array which has as much as the number of items
	bin_ar = [bin_capacity] * len(item_weights)

	#set result value which is the number of non-empty bin, so it is 0 at first
	num_nonempty_bin = 0

	for i in range(len(item_weights)):
		bin_index = 0			#when loop finds the minimum-leftover space bin, use this index for deducting space as much as weight of the indexed item
		minimum = bin_capacity	#indicator for minimum space
		j = 0

		while j < num_nonempty_bin:
			if bin_ar[j] - item_weights[i] >= 0 and bin_ar[j] - item_weights[i] < minimum:
				minimum = bin_ar[j] - item_weights[i]
				bin_index = j
			j += 1

	#a case for there is no enough space for indexed item (go to new bin)
		if minimum == bin_capacity:
			bin_ar[num_nonempty_bin] -= item_weights[i]
			num_nonempty_bin += 1

	#if there is enough space for indexed item, then deduction
		else:
			bin_ar[bin_index] -= item_weights[i]

	#return the number of non-emptied bins in the bin_ar
	return num_nonempty_bin

#main part
if __name__ == "__main__":
	bin_capacity = 10
	item_weights = [0] * random.randint(20, 5000)
	for i in range(len(item_weights)):
		item_weights[i] = random.randint(1,10)
	
	print("\n the algorithms will run 10 times each\n")
	#measure running time for each algorithm and then print results
	for j in range(10):
		start_time_1 = time.time()
		first_fit_res = first_fit(bin_capacity, item_weights)
		running_time_1 = str(time.time() - start_time_1)

		start_time_2 = time.time()
		first_fit_drecreasing_res = first_fit_drecreasing(bin_capacity, item_weights)
		running_time_2 = str(time.time() - start_time_2)

		start_time_3 = time.time()
		best_fit_res = best_fit(bin_capacity, item_weights)
		running_time_3 = str(time.time() - start_time_3)

	#print(f "") is for python 3.5 +, check python3 version
		print(f"The number of items {len(item_weights)} First Fit: {first_fit_res}, {running_time_1} seconds. First Fit Decreasing: {first_fit_drecreasing_res}, {running_time_2} seconds. Best Fit: {best_fit_res}, {running_time_3} seconds. ")

		
				

				
