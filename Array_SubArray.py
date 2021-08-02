# Prefix sums  -
# time complexity : O(N^2)
# space comlexity : O(N)

def prefixlargestsubarraysum(arr):
    prefix = [0]*len(arr)
    largest = 0
    prefix[0] = arr[0]
    for i in range(1, len(arr)):
        prefix[i] = prefix[i-1] + arr[i]
    for i in range(0, len(arr)):
        for j in range(1, len(arr)):
            subarraysum = prefix[j] - prefix[i-1] if i > 0 else prefix[j]
            largest = max(largest, subarraysum)
    return largest



# Kadane's Algorithm  - OPTIMAL
# time complexity : O(N)
# space comlexity : O(1) = 

def kadanelargestsubarraysum(arr):
    largest = 0      
    current = 0         
    for i in arr:
        current += i
        if current < 0:
            current = 0
        largest = max(largest, current)
    return largest


print(prefixlargestsubarraysum([5, -6, 5, -7, 4, 7, -6, 2, -1, 3]))
                        
print(kadanelargestsubarraysum([5, -6, 5, -7, 4, 7, -6, 2, -1, 3]))
                          # cur:5   0   5  0  4  11  5  7   6   9
                          # gre:5   5   5  5  5  11 11 11  11  11