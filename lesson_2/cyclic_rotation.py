"""
Task Score: 100%
Complexity: O(1)
"""


def solution(A, K):
    """
    In the below example we calculate the real value of K (by removing full
    loops) and then shift by K using list ranges.

    This could be also implemented by using the list.pop() method, however
    the time complexity would be greater (if somewhat more legible paraphs)

    Warning:
        Please keep in mind that an empty list is a perfectly valid input and
        should be handled properly.
    """
    # empty array, nothing to do
    if len(A) == 0:
        return A

    # get real shift coefficient
    K = K % len(A)

    # shift list to the right by K times
    return A[-K:] + A[:-K]
