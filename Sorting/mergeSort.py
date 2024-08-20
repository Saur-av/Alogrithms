
# #Let's learn how to sort two arrays using two pointes

def mergeSort(arr,s,e):
    if e - s +1<= 1:
        return
    
    mid = (s + e) // 2
    mergeSort(arr,s,mid)
    mergeSort(arr,s,mid + 1)
    
    merge(arr,s,mid,e)

def merge(arr,s,m,e):
    arr1 = arr[s : m + 1]
    arr2 = arr[m + 1 : e + 1]

    i = 0
    j = 0
    k = s

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[i]:
            arr[k] = arr1[i]
            i += 1
        if arr1[i] > arr2[i]:
            arr[k] = arr2[j]
            j += 1
        k += 1

    while i < len(arr1):
        arr[k] = arr1[i]
        k += 1
        i += 1

    while j < len(arr2):
        arr[k] = arr2[j]
        k += 1
        j += 1

mergeSort([1,2,3,4,5,6],0,6)