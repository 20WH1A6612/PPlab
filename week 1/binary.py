def binary(arr, key):
    a = 0
    b = len(arr - 1)
    while(a <= b):
        med = (a  + b) // 2
        if arr[med] == key:
            return med
        elif key < arr[mid]:
            b = med - 1
        elif key > arr[mid]:
            b = med + 1
    return -1

arr = [1, 2, 4. 6, 8, 9]
key = 
print("found" + str(binary(arr, key)))

