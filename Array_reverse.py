def reversearr1(arr):
    revarr = [0] * len(arr)
    for i in range(0, len(arr)):
        revarr[i] = arr[(len(arr)-1)-i]
    return revarr

#time Complexity: O(N)
#space Comlexity: O(N)
def reversearr(arr):
    n = len(arr)
    
    start = 0
    end = n - 1
    
    while (start < end):
        swap(arr, start, end)
        start += 1
        end -=1 
    return arr
        
def swap(arr, s, e):
    temp = arr[s]
    arr[s] = arr[e]
    arr[e] = temp


#time Complexity: O(N/2) => O(N)
#space Comlexity: O(1)
print(reversearr([1, 2, 3, 4, 5]))
print(reversearr1([1, 2, 3, 4, 5]))
