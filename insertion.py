def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

n = int(input("Enter number of elements: "))
data = []
for i in range(n):
    value = int(input(f"Enter element {i+1}: "))
    data.append(value)

print("The sorted elements are:", insertion_sort(data))
