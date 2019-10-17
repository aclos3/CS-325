# AUTHOR: Written by Junhyeok Jeong (jeongju@oregonstate.edu)
# ID: 933196042
# CLASS: CS325 - 400 (2019 Fall)
# ASSIGNMENT: Homework 1

import string
import numpy

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
			if int(left[i]) < int(right[j]):
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

		

with open("data.txt", "r") as f:
	for line in f:
		# make an array of each line in the data.txt with split function 
		line = line.split()
		
		#print the number of integer in a line
		print("the number of integer in one line: " + str(len(line)-1))
 
		#remove first element which is the number of integer in a line
		line.remove(line[0])
		#merge sort
		mergesort(line)

		#print sroted lines
		print("sorted line: " + str(line))
		
		#write insert.txt as sorting result
		with open("merge.txt", "a") as w:
			for k in range(len(line)):
				w.write(str(line[k]) + " ")
			w.write("\n")
		w.close()
	
	print("merge.txt file is created successfully !")

f.close()	

	
