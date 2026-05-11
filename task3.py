import timeit
import random


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def timsort(arr):
    return sorted(arr)


arr = [random.randint(1, 1000) for _ in range(1000)]

t1 = timeit.timeit(lambda: insertion_sort(arr.copy()), number=100)
t2 = timeit.timeit(lambda: merge_sort(arr.copy()), number=100)
t3 = timeit.timeit(lambda: timsort(arr.copy()), number=100)

print(f"Insertion sort: {t1:.4f} сек")
print(f"Merge sort:     {t2:.4f} сек")
print(f"Timsort:        {t3:.4f} сек")


# Висновки:
# 1. Timsort найшвидший бо поєднує переваги Merge sort і Insertion sort
# 2. Merge sort швидший за Insertion sort бо працює з половиною масиву (O n log n)
# 3. Insertion sort найповільніший на великих даних (O n²), 
#    але ефективний на МАЛЕНЬКИХ масивах або вже майже відсортованих даних
# 4. Саме тому програмісти використовують вбудований sorted() а не пишуть самі сортування, бо він оптимізований для різних випадків і працює швидко на великих даних.