"""
Task Score: 100%
Complexity: O(N * log(N))
"""


def is_triangle(a, b, c):
    # apply given formulate to triplet
    return a + b > c and \
           b + c > a and \
           a + c > b


def solution(A):
    """
    I am sure there is a mathematical proof for this somewhere, however I
    thought by looking at the problem that if there are three values that match
    the given criteria, they are most likely to be found in numbers that are
    very close together.

    Following that line of thought, I have solved this as follows:
    1. Order the array (ascending or descending does not matter here)
    2. Do a single pass and check consecutive values
    """
    # sort array
    A = sorted(A)

    for i in range(len(A) - 2):
        # check triplet
        if is_triangle(*A[i:i + 3]):
            return 1

    return 0
