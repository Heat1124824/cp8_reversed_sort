def reverse_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

def reverse_selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        max_index = i
        for j in range(i+1, n):
            if arr[j] > arr[max_index]:
                max_index = j
        if max_index != i:
            arr[i], arr[max_index] = arr[max_index], arr[i]

#numbers = [5, 42, 69, 30, 12]
numbers = [2, 6, 24, 27, 0]

print("原本的串列: ", numbers)
reverse_bubble_sort(numbers)
print("遞減氣泡排序法: ", numbers)
reverse_selection_sort(numbers)
print("遞減選擇排序法: ", numbers)