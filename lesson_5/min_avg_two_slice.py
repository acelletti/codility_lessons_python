"""
Task Score: 100%
Complexity: O(N)
"""
import sys


def solution(A):
    """
    This problem is very hard.

    At first attempt, the complexity of my solution was too high and I was
    frankly stumped to think of something that could improve the performance.

    However, after some googling, I found out that some smart person out
    there has not only figure this out but has written a proof on why us
    common mortals can safely consider only pairs and triplets when looking
    at the possible combinations.

    The proof can be found here: https://github.com/daotranminh/playground/blob/master/src/codibility/MinAvgTwoSlice/proof.pdf

    So based on what I said before, check both pairs and triplets as you iterate
    through the list and record the first occurrence of the smallest mean and its
    index.
    """
    # create variables to record lowest mean and index
    lowest_idx, lowest_mean = 0, sys.maxsize

    # iterate for 0 < i < N -1, so we can look at pairs
    for i in range(len(A) - 1):

        # get mean of current pair of 2
        current_mean = (A[i] + A[i + 1]) / 2

        # update lowest pointers if needed
        if current_mean < lowest_mean:
            lowest_mean = current_mean
            lowest_idx = i

        # if not at the end of the list
        if i < len(A) - 2:

            # get mean of current pair of 3
            current_mean = (A[i] + A[i + 1] + A[i + 2]) / 3

            # update lowest pointers if needed
            if current_mean < lowest_mean:
                lowest_mean = current_mean
                lowest_idx = i

    return lowest_idx
