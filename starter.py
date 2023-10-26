import radix, quicksort, insertion, countSort, mergeSort
import time, random as r
import matplotlib.pyplot as plt

def Timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        elapsed_time = time.perf_counter() - start
        print(f"{func.__name__} time: {elapsed_time*1000:.4f}ms")
        return elapsed_time*1000
    return wrapper


def makeTimeArray(sorts: dict):
    arr = {}
    for name in sorts.keys():
        if sorts[name]:
            arr.update({name: []})
    return arr


def Printif(sorted, flag):
    if flag:
        print(sorted)


def generateArr(maxLen, count):
    arr = []
    for n in range(count):
        arr.append(r.randint(0,10**maxLen-1))
    return arr

class Sorts:
    def __init__(self, arr, print=False):
        self.arr = arr
        self.print = print

    @Timer
    def radixLSD(self):
        Printif(radix.radixLSD(self.arr.copy()), self.print)

    @Timer
    def quickSort(self):
        Printif(quicksort.quickSort(self.arr.copy()), self.print)

    @Timer
    def insertionSort(self):
        Printif(insertion.insertionSort(self.arr.copy()), self.print)

    @Timer
    def countSort(self):
        Printif(countSort.countSort(self.arr.copy()), self.print)

    @Timer
    def mergeSort(self):
        Printif(mergeSort.mergeSort(self.arr.copy()), self.print)


chooseSorts = {
    "radixLSD": True,
    "quickSort": True,
    "insertionSort": True,
    "countSort": True,
    "mergeSort": True
}

if __name__ == "__main__":
    times = makeTimeArray(chooseSorts)
    repetitions = 7
    step = 1000

    for n in range(1,repetitions):
        s = Sorts(generateArr(7 , n*step)) # generate random int list (N of digits, amount)
        #s = Sorts([21, 35, 56, 41, 24, 88, 6, 11, 57, 15]) # add ",True)" to display sort outputs
        for name in times.keys():
            times[name].append(eval(f"s.{name}()"))

    sizes = [n*step for n in range(1,repetitions)]
    for name in times.keys():
        plt.plot(sizes, times[name], label=name)

    plt.xlabel("Размер массива")
    plt.ylabel("Время выполнения (мс)")
    plt.title("Зависимость времени выполнения от размера массива")
    plt.legend()
    plt.grid()
    plt.show()