# AUTHOR: Written by Junhyeok Jeong (jeongju@oregonstate.edu)
# ID: 933196042
# CLASS: CS325 - 400 (2019 Fall)
# ASSIGNMENT: Homework 3

import string
import numpy

def modified_knapsack(member_weight, item_weight, item_price, item_num, case):
    total_price = 0
    picked_item = []
    #picked_item = [[0 for col in range(len(member_weight))] for row in range(len(member_weight))]
    for a in range(len(member_weight)):
        #initialize table K of 0-1 knapsack
        K = [[0 for col in range(member_weight[a]+1)] for row in range(item_num+1)]

        #0-1 knapsack algorithm with max() function
        for i in range(item_num+1):
                for j in range(member_weight[a]+1):
                        if i == 0 or j == 0:
                            K[i][j] = 0
                        elif item_weight[i-1] <= j:
                            K[i][j] = max(item_price[i-1] + K[i-1][j - item_weight[i-1]], K[i-1][j])
                        else:
                            K[i][j] = K[i-1][j]

        #a family member's optimized price is stored on the last element on table K
        max_price = K[item_num][member_weight[a]]
        total_price = total_price + max_price

        max_index = member_weight[a]
        picked_ar = []

        for k in range(item_num, 0, -1):
        #if a member can't carry, then break loop
            if max_price <= 0:
                break

            if max_price == K[k-1][max_index]:
                continue
            else:
        #append picked item's weight on result array
                picked_ar.append(k)


        #the price should be deducted by weight loss
                max_price = max_price - item_price[k-1]
                max_index = max_index - item_weight[k-1]

        picked_item.append(sorted(picked_ar))

    #write the results on results.txt
    with open("results.txt", "a") as w:
        w.write("Test Case {0}\nTotal Price {1}\n".format(case, total_price))
        w.write("Member Items:\n")
        for x in range(len(member_weight)):
            w.write("{0}: ".format(x+1))
            w.write("{0}\n".format(' '.join(map(str, picked_item[x]))))
        w.write("\n")

    print("Test case {0} is written on results.txt successfully!".format(case))

#main part
with open("shopping.txt", "r") as f:
    mylines = []
    file_size = 0
    #read and copy every line on an array called 'mylines'
    for i, line in enumerate(f):
        file_size = i
        mylines.append(line.strip())

    #pop the first element of 'mylines' which is the number of case
    mylines.pop(0)

    case = 1
    index = 0
    while index < len(mylines):
    #initialize arrays for storing item infomation and family information
        price = []
        weight = []
        family_capacity = []
        item_ea = int(mylines[index])
        index += 1

    #store item price and weight on two arrays
        for j in range(item_ea):
            item_info = mylines[index].split()
            price.append(int(item_info[0]))
            weight.append(int(item_info[1]))
            index += 1

    #store family weight capacity on an array
        family_num = int(mylines[index])
        index += 1
        for k in range(family_num):
            family_capacity.append(int(mylines[index]))
            index += 1

        modified_knapsack(family_capacity, weight, price, item_ea, case)

        case += 1

f.close()
