def closestsubarraysum(arr, x):
    closest = arr[0] + arr[1]
    for i in range(0, len(arr)):
        for j in range(1, len(arr)):
            if (arr[i] + arr[j]) < x and (arr[i] + arr[j] > closest):
                    closest = arr[i] + arr[j]
    return closest

print(closestsubarraysum([10,22,28,29,30,40],54))
            
1