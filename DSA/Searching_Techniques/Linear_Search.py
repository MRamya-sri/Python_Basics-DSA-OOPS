# Linear Searching
arr = [2, 5, 3, 8, 9, 31]
targetVal = 9

def LinearSearch(arr, targetVal):
    for i in range(len(arr)):
        if arr[i] == targetVal:
            return i
    return -1

result = LinearSearch(arr, targetVal)

if result != -1:
    print(f'Value {targetVal} is found at the index {result}')
else:
    print(f"Didn't find the value {targetVal} at any index in array.")