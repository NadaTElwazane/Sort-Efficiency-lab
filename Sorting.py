# Quick sort algorithm in python
import random
import time
import matplotlib.pyplot as plt

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
def findKthSmallest(arr, k):
    low = 0
    high = len(arr) - 1
    pi = partition(arr, low, high)
    while low <= high:
        if pi == k-1:
            return arr[pi]
        elif pi < k:
            pi = partition(arr, pi+1, high)
        else:
            pi = partition(arr, low, pi-1)


# test quick sort
# random array of size 100
list_length=[100,200,500,1000,10000,25000,50000,100000]
time_in_microseconds_insertion_sort = [0]*len(list_length)
time_in_microseconds_selection_sort = [0]*len(list_length)
time_in_microseconds_merge_sort = [0]*len(list_length)
time_in_microseconds_quick_sort = [0]*len(list_length)
time_in_microseconds_merge_sort_threshold = [0]*len(list_length)
time_in_microseconds_find_kth_smallest = [0]*len(list_length)
for i in list_length:
    print("array of length:",i)
    array = [random.randint(0, i*100) for i in range(i)]
    array1 = array.copy()
    array2 = array.copy()
    array3 = array.copy()
    array4 = array.copy()
    array5 = array.copy()
    #Quick sort
    start_time=time.time_ns()//1000
    quick_sort(array, 0, len(array) - 1)
    end_time=time.time_ns()//1000
    time_in_microseconds_quick_sort[list_length.index(i)]=end_time-start_time
    print("Quick sort time:",end_time-start_time, "microseconds")
    #Merge sort
    start_time=time.time_ns()//1000
    merge_sort(array1, 0, len(array1) - 1)
    end_time=time.time_ns()//1000
    time_in_microseconds_merge_sort[list_length.index(i)]=end_time-start_time
    print("Merge sort time:",end_time-start_time, "microseconds")
    #Insertion sort
    start_time=time.time_ns()//1000
    insertion_sort(array2)
    end_time=time.time_ns()//1000
    time_in_microseconds_insertion_sort[list_length.index(i)]=end_time-start_time
    print("Insertion sort time:",end_time-start_time,"microseconds")
    #Selection sort
    start_time=time.time_ns()//1000
    selection_sort(array3)
    end_time=time.time_ns()//1000
    time_in_microseconds_selection_sort[list_length.index(i)]=end_time-start_time
    print("Selection sort time:",end_time-start_time,"microseconds")
    # Hybrid Merge sort and selection sort
    start_time=time.time_ns()//1000
    hybrid_merge_selection_sort(array4, 0, len(array4) - 1, 3)
    end_time=time.time_ns()//1000
    time_in_microseconds_merge_sort_threshold[list_length.index(i)]=end_time-start_time
    print("Hybrid Merge sort and selection sort time:",end_time-start_time,"microseconds")
    #Find kth smallest element
    start_time=time.time_ns()//1000
    K = findKthSmallest(array5, 3)
    end_time=time.time_ns()//1000
    time_in_microseconds_find_kth_smallest[list_length.index(i)]=end_time-start_time
    print("Kth Smallest element:", K)
    print("Find kth smallest element time:",end_time-start_time,"microseconds")
    print("First 10 elements:",array4[:10])
    if array == sorted(array) and array1 == sorted(array1) and array2 == sorted(array2) and array3 == sorted(
            array3) and array4 == sorted(array4):
        print("Sorting is correct")
    else:
        print("Sorting is incorrect")

#plotting the time taken for each sort
plt.plot(list_length,time_in_microseconds_insertion_sort,label="Insertion sort")
plt.plot(list_length,time_in_microseconds_selection_sort,label="Selection sort")
plt.plot(list_length,time_in_microseconds_merge_sort,label="Merge sort")
plt.plot(list_length,time_in_microseconds_quick_sort,label="Quick sort")
plt.plot(list_length,time_in_microseconds_merge_sort_threshold,label="Hybrid Merge sort and selection sort")
plt.plot(list_length,time_in_microseconds_find_kth_smallest,label="Find kth smallest element")
plt.xlabel("Array length")
plt.ylabel("Time in microseconds")
plt.legend()
plt.show()

