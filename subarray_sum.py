'''
This problem is taken from Stanford's CS 9: Problem-Solving for
                                            the CS Technical Interview.
http://web.stanford.edu/class/cs9/sample_probs/SubarraySums.pdf

A subarray of an array is a consecutive sequence of zero or more values taken
out of that array. For example, the array [1, 3, 7] has seven subarrays:
[ ] [1] [3] [7] [1, 3] [3, 7] [1, 3, 7]

Notice that [1, 7] is not a subarray of [1, 3, 7], because even though the
values 1 and 7 appear in the array, they're not consecutive in the array.

Similarly, the array [7, 3] isn't a subarray of the original array,
because these values are in the wrong order.

The sum of an array is the sum of all the values in that array. Your task is
to write a function that takes as input an array and outputs the sum of all of
its subarrays.

For example, given [1, 3, 7], you'd output 36, because:

[ ] + [1] + [3] + [7] + [1, 3] + [3, 7] + [1, 3, 7]
= 0 + 1 + 3 + 7 + 4 + 10 + 11 = 36

My solution:
    subarray_sum_slow: the easy but slow way to do it. Just enumberate all the
                       subarrays and sum them up.
    subarray_sum: the fast way to do it. We can calculate the number of times
                  each element occurs and sum them up.
'''


def get_subarrays(arr):
    subarrays = []
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            subarrays.append(arr[i:j + 1])
    return subarrays


def subarray_sum_slow(arr):
    subarrays = get_subarrays(arr)
    return sum([sum(arr) for arr in subarrays])


def subarray_sum(arr):
    total = 0
    for i, num in enumerate(arr):
        total += num * (i + 1) * (len(arr) - i)
    return total


assert subarray_sum_slow([1]) == subarray_sum([1])
assert subarray_sum_slow([1, 2]) == subarray_sum([1, 2])
assert subarray_sum_slow([1, 2, 3]) == subarray_sum([1, 2, 3])
assert subarray_sum_slow([1, 3, 7]) == subarray_sum([1, 3, 7])
assert subarray_sum_slow([1, 3, 7, 9]) == subarray_sum([1, 3, 7, 9])
assert subarray_sum_slow([1, 3, 7, 9, 11]) == subarray_sum([1, 3, 7, 9, 11])
assert subarray_sum_slow(
    [1, 3, 7, 9, 11, 13]) == subarray_sum([1, 3, 7, 9, 11, 13])
