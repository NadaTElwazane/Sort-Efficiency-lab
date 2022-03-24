# Quick sort algorithm in python
import random


def partition(array, low, high):
    # random pivot
    pivot = random.randint(low, high)
    array[pivot], array[high] = array[high], array[pivot]
    i = low - 1
    for j in range(low, high):
        if array[j] <= array[high]:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)


# Merge sort algorithm in python
def merge(array, low, mid, high):
    nL = mid - low + 1
    nR = high - mid
    L = [0] * (nL)
    R = [0] * (nR)
    for i in range(0, nL):
        L[i] = array[low + i]
    for j in range(0, nR):
        R[j] = array[mid + 1 + j]  # mid+1 start of right array
    i = 0
    j = 0
    k = low
    while i < nL and j < nR:
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1
    while i < nL:
        array[k] = L[i]
        i += 1
        k += 1
    while j < nR:
        array[k] = R[j]
        j += 1
        k += 1


def merge_sort(array, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(array, low, mid)
        merge_sort(array, mid + 1, high)
        merge(array, low, mid, high)


# insertion sort algorithm in python
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i
        while j > 0 and key < array[j - 1]:
            array[j] = array[j - 1]
            j -= 1
        array[j] = key


# selection sort algorithm in python
def selection_sort(array):
    for i in range(0, len(array) - 1):  # not including last element
        min = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min]:
                min = j
        if min != i:
            array[i], array[min] = array[min], array[i]
    return array


def hybrid_merge_selection_sort(array, low, high, threshold):
    if high - low + 1 <= threshold:
        array[low:high + 1] = selection_sort(array[low:high + 1])  # from low to high
    else:
        mid = (low + high) // 2
        hybrid_merge_selection_sort(array, low, mid, threshold)
        hybrid_merge_selection_sort(array, mid + 1, high, threshold)
        merge(array, low, mid, high)


# Kth smallest element in an array using partition from quick sort
def kth_smallest(array, low, high, k):
    if low < high:
        pi = partition(array, low, high)
        if pi > k - 1:
            kth_smallest(array, low, pi - 1, k)
        elif pi < k - 1:
            kth_smallest(array, pi + 1, high, k)
    return array[pi]

# test quick sort
# random array of size 100
array = [random.randint(0, 10000) for i in range(10)]
array1 = array.copy()
array2 = array.copy()
array3 = array.copy()
array4 = array.copy()
array5 = array.copy()
quick_sort(array, 0, len(array) - 1)
merge_sort(array1, 0, len(array1) - 1)
insertion_sort(array2)
selection_sort(array3)
hybrid_merge_selection_sort(array4, 0, len(array4) - 1, 3)
K = kth_smallest(array5, 0, len(array5) - 1, 4)
print(K)
print(array5)

if array == sorted(array) and array1 == sorted(array1) and array2 == sorted(array2) and array3 == sorted(
        array3) and array4 == sorted(array4):
    print("Sorting is correct")
else:
    print("Sorting is incorrect")

print("Array", array5)
