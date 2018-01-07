# Lomuto algorithm is easier to implement
# Hoare algorithm is more efficient because it has fewer swaps.
# Hoare algorithms partition is more effective than lomuto's
# When same array is sorted with lomuto and hoare, hoare never swaps
# but lomuto will swap elements, so hoare is more efficient.
def partitionLomuto(arr, start, end):
    index = start  # index of smaller element
    pivot = arr[start]  # pivot
    for j in range(start+1, end):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            index += 1
            arr[index], arr[j] = arr[j], arr[index]

    arr[index], arr[start] = arr[start], arr[index]
    return index

def partitionHoare(arr, start, end):
    left = start + 1
    right = end
    while True:

        while arr[left] < arr[start]:
            # find item on left to swap
            left += 1
            if left >= end:
                break

        while arr[right] > arr[start]:
            # find item on right to swap
            right -= 1
            if right <= start:
                break

        # if we have already gone through all arr
        if left >= right:
            break

        # swap arr
        arr[left], arr[right] = arr[right], arr[left]

    # swap partitioning item with the biggest on the left side (which is less than lo)
    arr[start], arr[right] = arr[right], arr[start]
    return right


def quickSortLomuto(arr):
    qsl = arr
    LomutoQuickSort(qsl,0,len(qsl)-1)
    return qsl

def quickSortHoare(arr):
    qsh = arr
    HoareQuickSort(qsh,0,len(qsh)-1)
    return qsh

# The main function that implements QuickSort
# Function to do Quick sort with Lumoto
def LomutoQuickSort(arr, start, end):
    if start < end:
        # pi is partitioning index, arr[p] is now
        # at right place
        pivot = partitionLomuto(arr, start, end)

        # Separately sort elements before
        # partition and after partition
        LomutoQuickSort(arr, start, pivot - 1)
        LomutoQuickSort(arr, pivot + 1, end)

# Function to do Quick sort with hoare partition
def HoareQuickSort(arr, start, end):
    if start < end:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partitionHoare(arr, start, end)

        # Separately sort elements before
        # partition and after partition
        LomutoQuickSort(arr, start, pi - 1)
        LomutoQuickSort(arr, pi + 1, end)

arr = [15,4,68,24,75,16,42]
qsh = quickSortHoare(arr)
print(qsh)

#Output: [4, 15, 16, 24, 42, 68, 75]
qsl = quickSortLomuto(arr)
print(qsl)
#Output: [4, 15, 16, 24, 42, 68, 75]