"""
Task Score: 100%
Complexity: O(N)
"""
import collections


def solution(A):
    """
    This is super easy, no comments needed.
    """
    # check for empty array
    if not len(A):
        return -1

    # get leader and number of occurrences for A
    leader, occurrences = collections.Counter(A).most_common(1)[0]

    # check if it is a leader
    if occurrences <= len(A) / 2:
        return -1

    # return first index
    return A.index(leader)
