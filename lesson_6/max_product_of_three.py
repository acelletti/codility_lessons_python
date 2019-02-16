"""
Task Score: 100%
Complexity: O(N * log(N))
"""


def solution(A):
    """
    On the face of it this is quite simple, until you factor in negative
    numbers.

    Approach is very simple:
    1. Sort array in descending order (or ascending if you like)
    2. Take the max value in between the sum of the head of the array and the first
        element of the array combined with the last two elements (two negatives)
    """
    # sort array in descending order
    A = sorted(A, reverse=True)

    # get the product of the first three elements
    return max(A[0] * A[1] * A[2], A[0] * A[-2] * A[-1])
