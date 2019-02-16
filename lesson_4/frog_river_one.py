"""
Task Score: 100%
Complexity: O(N)
"""


def solution(X, A):
    """
    For this task, we simply need to record where the leaves have fallen.

    As soon as we have a bridge, we cross.
    """
    # initialise variables to keep track of the leaves
    leaves = [False] * X
    leaves_count = 0

    for idx, val in enumerate(A):

        # leaf has fallen on an empty spot
        if not leaves[val - 1]:

            # increase counter
            leaves_count += 1

            # bridge is complete, we can cross
            if leaves_count == X:
                return idx

            # record the space as filled
            leaves[val - 1] = True

    # the frog is stuck on this side I'm afraid
    return -1
