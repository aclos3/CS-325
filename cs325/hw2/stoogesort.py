# AUTHOR: Written by Junhyeok Jeong (jeongju@oregonstate.edu)
# ID: 933196042
# CLASS: CS325 - 400 (2019 Fall)
# ASSIGNMENT: Homework 2

import string
import numpy

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
		



with open("data.txt", "r") as f:
	for line in f:
		# make an array of each line in the data.txt with split function 
		line = line.split()
		
		#print the number of integer in a line
		print("the number of integer in one line: " + str(len(line)-1))
 
		#remove first element which is the number of integer in a line
		line.remove(line[0])
		#merge sort
		stoogesort(line, 0, len(line)-1)

		#print sroted lines
		print("sorted line: " + str(line))
		
		#write stooge.txt as sorting result
		with open("stooge.txt", "a") as w:
			for k in range(len(line)):
				w.write(str(line[k]) + " ")
			w.write("\n")
		w.close()
	
	print("stooge.txt file is created successfully !")

f.close()	

	
