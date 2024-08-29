def binarySearch(arr, targetVal):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left+right)//2

        if arr[mid] == targetVal:
            return mid
        
        if arr[mid] < targetVal:
            left = mid+1
        else:
            right = mid-1 
    
    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 23, 42, 56, 90]
targetVal = 23

result = binarySearch(arr, targetVal)

if result != -1:
    print(f'Value {targetVal} is found in the index {result}')
else:
    print(f"Value {targetVal} not found!")
