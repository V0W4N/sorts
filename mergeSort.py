
class MergeSort:
    def __init__(self):
        pass

    def mergeSort(self, arr):
        self.mergeSortCycle(arr)
        return arr

    def mergeSortCycle(self, arr):
        if len(arr) > 1:

            # Create sub_array2 ← A[start..mid] and sub_array2 ← A[mid+1..end]
            mid = len(arr) // 2
            sub_array1 = arr[:mid]
            sub_array2 = arr[mid:]

            # Sort the two halves
            self.mergeSortCycle(sub_array1)
            self.mergeSortCycle(sub_array2)

            # Initial values for pointers that we use to keep track of where we are in each array
            i = j = k = 0

            # Until we reach the end of either start or end, pick larger among
            # elements start and end and place them in the correct position in the sorted array
            while i < len(sub_array1) and j < len(sub_array2):
                if sub_array1[i] < sub_array2[j]:
                    arr[k] = sub_array1[i]
                    i += 1
                else:
                    arr[k] = sub_array2[j]
                    j += 1
                k += 1

            # When all elements are traversed in either arr1 or arr2,
            # pick up the remaining elements and put in sorted array
            while i < len(sub_array1):
                arr[k] = sub_array1[i]
                i += 1
                k += 1

            while j < len(sub_array2):
                arr[k] = sub_array2[j]
                j += 1
                k += 1



def mergeSort(arr):
    m = MergeSort()
    return m.mergeSort(arr)

