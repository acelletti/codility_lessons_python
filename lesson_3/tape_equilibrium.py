"""
Task Score: 100%
Complexity: O(N)
"""


def solution(A):
    """
    """
    # initialise array to record the sums of the elements in the array
    sum = [0] * len(A)
    sum[0] = A[0]

    # populate sums
    for i in range(1, len(A)):
        sum[i] = A[i] + sum[i - 1]

    # get a list of solutions for valid values of N
    solutions = [abs(sum[-1] - 2 * sum[i])
                 for i in range(0, len(A) - 1)]

    # return smallest value found
    return min(solutions)
