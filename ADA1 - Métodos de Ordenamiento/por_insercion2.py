def insertion_sort_strings(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

strings = ["banana", "apple", "orange", "grape", "pineapple"]
insertion_sort_strings(strings)
print("Lista ordenada:")
for s in strings:
    print(s, end=" ")
