# AUTHOR: Written by Junhyeok Jeong (jeongju@oregonstate.edu)
# ID: 933196042
# CLASS: CS325 - 400 (2019 Fall)
# ASSIGNMENT: Homework 4

import string
import numpy

# set up Activity class for storing activity information
class Activity:
	def __init__(self, activity_num, start_time, end_time):
		self.activity_num = activity_num
		self.start_time = start_time
		self.end_time = end_time

def reverse_merge_sort(arr):
	#finding half and then divide into left and right of the input array
	if len(arr) > 1:
		half = len(arr) // 2
		left = arr[:half]
		right = arr[half:]

		reverse_merge_sort(left)
		reverse_merge_sort(right)

		i = j = k = 0
		
		#if left element is bigger than right one, then put the value in the original array
		while i < len(left) and j < len(right):
			if left[i].end_time > right[j].end_time:
				arr[k] = left[i]
				i += 1
			else:
				arr[k] = right[j]
				j += 1
			k += 1

		#if there is leftover, then put the value into left side first
		while i < len(left):
			arr[k] = left[i]
			k += 1
			i += 1
		while j < len(right):
			arr[k] = right[j]
			k += 1
			j += 1
	
def last_to_first(activities, slot):
	res = []
	i = 0
	res.append(activities[0].activity_num)

	#if start time of element is bigger than end time of element, then append at result array 
	for j in range(1,len(activities)):
		if activities[i].start_time >= activities[j].end_time:
			res.append(activities[j].activity_num)
			i = j

	res = list(res[a] for a in range(len(res)-1, -1, -1))
	return res

#main part
mylines = []

#store all lines from a text file in an array
with open("act.txt", "r") as f:
	for i,line in enumerate(f): 
		mylines.append(line.strip())

f.close()

case = 1
line_index = 0

# with while loop, separate the data in the 'mylines'
while line_index < len(mylines):
	activity_ea = int(mylines[line_index])
	slot = [] 
	activities = []
	line_index += 1

#separate data based on the class attributes
	for i in range(activity_ea):
		activity_info = list(map(int, mylines[line_index].split()))
		temp = Activity(activity_info[0], activity_info[1], activity_info[2])
		activities.append(temp)
		line_index += 1
	
	# sort the activity array in desending order of end time
	reverse_merge_sort(activities)

	res = last_to_first(activities, slot)

	print("Set {0}\nNumber of activities selected = {1} \nActivities: {2}\n".format(case, len(res), " ".join(map(str, res))))
	case += 1




