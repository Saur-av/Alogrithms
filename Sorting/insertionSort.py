#My Approach : Time Complexity O(N ^ 2)

import random

def insersionSort(arr : list):
    print("Initial Array: \n",arr)

    for i in range(1 , len(arr)):
        # print(i,arr)

        for j in range(i,0 ,-1):
            if arr[j] >= arr[j - 1]:
                break
            temp = arr[j]
            arr[j] = arr[j - 1]
            arr[j - 1] = temp

    print("Sorted Array: \n",arr)

insersionSort([random.randint(0,100) for i in range(10)])
