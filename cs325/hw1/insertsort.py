# AUTHOR: Written by Junhyeok Jeong (jeongju@oregonstate.edu)
# ID: 933196042
# CLASS: CS325 - 400 (2019 Fall)
# ASSIGNMENT: Homework 1

import string
import numpy

with open("data.txt", "r") as f:
	for line in f:
		# make an array of each line in the data.txt with split function 
		line = line.split()
		
		#print the number of integer in a line
		print("the number of integer in one line: " + str(len(line)-1)) 
		
		#insertion sort process with a key
		for i in range(2, len(line)):
			insertion_key = line[i]
			j = i - 1
			
			while j >= 1 and int(insertion_key) < int(line[j]):
				line[j+1] = line[j]
				j = j - 1
			line[j+1] = insertion_key
		
		#remove first element which is the number of integer in a line
		line.remove(line[0])
		#print sorted lines
		print("sorted line: " + str(line))
		
		#write insert.txt as sorting result
		with open("insert.txt", "a") as w:
			for k in range(len(line)):
				w.write(str(line[k]) + " ")
			w.write("\n")
		w.close()
	
	print("insert.txt file is created successfully !")

f.close()	

			
			


