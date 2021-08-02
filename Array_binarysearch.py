def binarysearch(arr,key,start, end):
    n = len(arr)
    if key not in arr:
        return "Not Found"
    # while (start <= end):
    #     mid = int((start+end) / 2)d
    #     if arr[mid] < key:
    #         start = mid+1

    #     elif arr[mid] > key:
    #         end = mid-1 
    #     else:
    #         return mid
    mid = int((start+end) / 2)
    if arr[mid] < key:
         mid + 1
        binarysearch(arr, key, start, end)
    elif arr[mid] > key:
        end = mid - 1
        binarysearch(arr, key, start, end)
    else:
        return mid
# time complexity :  O(log(n))
# fast and efficient if array is monotonic        
print(binarysearch([2,4,5,9,11,15,17],17 , 0, 7))
