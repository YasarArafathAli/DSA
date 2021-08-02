def lowerbound(arr, val):
    lowerbound = arr[0]
    for i in arr:
        if i < val and i > lowerbound:
                lowerbound = i
    return lowerbound
# time complexity : 0(N)
#  space complecity : O(1)

# def upperbound(arr, val):
#     upperbound = val+1
#     for i in arr:
#         if i > val and i < upperbound:
#                 upperbound = i
#     return upperbound


print(lowerbound([-1,-1,3,2,-1,5],4))
print(upperbound([-1,-1,3,2,-1,6,7,8],4))