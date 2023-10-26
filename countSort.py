def countSort(arr):
    # Finding the maximum element of input_array.
    M = max(arr)

    # Initializing countArr with 0
    countArr = [0] * (M + 1)

    # Mapping each element of input_array as an index of countArr
    for num in arr:
        countArr[num] += 1

    # Calculating prefix sum at every index of countArr
    for i in range(1, M + 1):
        countArr[i] += countArr[i - 1]

    # Creating output_array from countArr
    output_array = [0] * len(arr)

    for i in range(len(arr) - 1, -1, -1):
        output_array[countArr[arr[i]] - 1] = arr[i]
        countArr[arr[i]] -= 1

    return output_array