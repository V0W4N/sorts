import random as r
def max_heapify(A,k, n):
    l = left(k)
    r = right(k)
    if l < n and A[l] > A[k]:
        largest = l
    else:
        largest = k
    if r < n and A[r] > A[largest]:
        largest = r
    if largest != k:
        A[k], A[largest] = A[largest], A[k]
        max_heapify(A, largest, n)

def left(k):
    return 2 * k + 1

def right(k):
    return 2 * k + 2

def build_max_heap(A):
    n = int((len(A)//2)-1)
    for k in range(n, -1, -1):
        max_heapify(A,k, len(A))

def heapSort(arr):
    n = len(arr)
    for i in range(n - 1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, 0, i)

def insert(A, x):
    A.append(x)
    build_max_heap(A)


#A = [r.randint(0,100) for _ in range(10)]
A = [21, 35, 56, 41, 24, 88, 6, 11, 57, 15]
build_max_heap(A)
insert(A, 40)
print(A)
heapSort(A)
print(A)
