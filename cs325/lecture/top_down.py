import math
import string
import time
import numpy

def factorial(dp, x):	
	if x == 0:
		return 1
	#if(dp[x] != -1):
	#	return dp[x]
	dp[x] = x * factorial(dp, x -1) 
		
	return dp[x]

dp = [0 for i in range(200)]
x = len(dp)-1

start_time = time.time()
factorial(dp,x)

print(dp[x])
print( "--- %s seconds ---" % (time.time() - start_time))
