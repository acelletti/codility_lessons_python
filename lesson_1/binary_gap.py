"""
Task Score: 100%
Complexity: O(N)
"""


def solution(N):
    """
    This is a fairly simple task.

    What we need to do is:
    1. Get string representation in binary form (I love formatted string literals)
    2. Measure biggest gap of zeroes (pretty self explanatory)
    """

    # get binary representation of number
    binary_repr = f"{N:b}"

    # initialise counters
    current_gap, max_gap = 0, 0

    for b in binary_repr:
        # end of gap, update max
        if b == '1':
            max_gap = max(current_gap, max_gap)
            current_gap = 0
        # increase gap counter
        else:
            current_gap += 1

    return max_gap
