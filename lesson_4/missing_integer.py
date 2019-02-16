"""
Task Score: 100%
Complexity: O(N * log(N))
"""
import collections


def solution(A):
    """
    I am starting to think that the people that write these problems have a
    special fondness for the Counter class.

    We simply iterate through the list of values that should be there and if
    any is missing we return it otherwise we return the size of the list + 1.
    """
    # get counter for array
    counter = collections.Counter(A)

    # get range of expected elements
    for i in range(1, len(A) + 1):

        # element missing
        if counter[i] == 0:
            return i

    # empty array or no missing element
    return len(A) + 1
