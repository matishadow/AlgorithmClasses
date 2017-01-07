import queue
import Labs.Lab1
import math


def counting_sort(A, result_array, k):
    l = len(A)

    result_array = [None] * l
    auxiliary_array = [None] * (k + 1)

    for i in range(0, k + 1):
        auxiliary_array[i] = 0

    for j in range(1, l + 1):
        auxiliary_array[A[j - 1]] += 1

    for i in range(1, k + 1):
        auxiliary_array[i] = auxiliary_array[i] + auxiliary_array[i - 1]

    for i in range(l, 0, -1):
        result_array[auxiliary_array[A[i - 1]] - 1] = A[i - 1]
        auxiliary_array[A[i - 1]] -= 1

    return result_array


def radix_sort_words(array):
    d = len(str(array[0]))
    n = len(array)

    queues = []
    for i in range(26):
        queues.append(queue.Queue())

    for k in range(1, d + 1):
        for j in range(1, n + 1):
            word = array[j - 1]
            character = word[d - k]

            queues[ord(character) - ord('A')].put_nowait(array[j - 1])

        array_index = 0
        for j in range(1, 26 + 1):
            q = queues[j-1]

            while len(q.queue) > 0:
                array[array_index] = q.get_nowait()
                array_index += 1


def bucket_sort(array, n):
    buckets = []
    for _ in range(n):
        buckets.append([])

    for i in range(0, len(array)):
        buckets[math.floor(n*array[i])].append(array[i])

    for bucket in buckets:
        Labs.Lab1.insertion_sort(bucket)

    for bucket in buckets:
        for i in bucket:
            print(i, end=', ')
