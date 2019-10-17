import numpy
import string
import math
import time

#top-down DP example (factorial)

dp= [0 for i in range(200)]

#base case

dp[0] = 1
n = len(dp) - 1
i = 1

start_time = time.time()
while i <= n:

	dp[i] = dp[i-1] * i
	i +=1

print(dp[n])
print("--- %s seconds ---" % (time.time() - start_time))
