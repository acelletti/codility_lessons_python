"""
Task Score: 100%
Complexity: O(N * log(N))
"""
import collections


def solution(A):
    """
    This is very simple if we use again our trusty Counter from collections.

    We simply iterate through the list of values that should be there and if
    any is missing we return 0 otherwise we return 1.

    I personally would not approve of this code in a code review as it
    clearly should return a bool value rather than an int, not sure what the
    rationale behind that is TBH.
    """
    # get counter for array
    counter = collections.Counter(A)

    # get range of permutations
    for i in range(1, len(A) + 1):

        # element missing, not a permutation
        if counter[i] == 0:
            return 0

    # all fine, it was a permutation
    return 1
