def radixLSD(source):
    RADIX = 10
    buckets = [[] for _ in range(RADIX)]
    maxLength = False
    placement = 1
    while not maxLength:
        maxLength = True

        # split input between lists
        for i in source:
            tmp = i // placement
            buckets[tmp % RADIX].append(i)
            if tmp > 0 and maxLength:
                maxLength = False

        # empty lists into input array
        a = 0
        for bucket in buckets:
            for i in bucket:
                source[a] = i
                a += 1
            bucket.clear()

        # move to next digit
        placement *= RADIX
    return source

