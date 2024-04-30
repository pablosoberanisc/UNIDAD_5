def selection_sort_strings(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

strings = ["banana", "apple", "orange", "grape", "pineapple"]
selection_sort_strings(strings)
print("Lista ordenada:")
for s in strings:
    print(s, end=" ")
