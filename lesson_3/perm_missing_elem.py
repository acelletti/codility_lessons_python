"""
Task Score: 100%
Complexity: O(N * log(N))
"""
import collections


def solution(A):
    """
    This can be easily implemented by taking advantage of the
    collections.Counter object. We can then iterate through the valid sequence
    and return the first number that cannot be found in the counter.

    Warning:
        With this problem we need to pay special care with two valid edge cases:
        1. Empty list (result should be 1)
        2. List with no missing element (result should be N+1)

    """
    # get counter for array
    counter = collections.Counter(A)

    # iterate from 1 - N
    for i in range(1, len(A) + 1):

        # found the missing element
        if counter[i] == 0:
            return i

    # not found, must be N + 1
    return len(A) + 1
