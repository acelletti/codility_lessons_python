"""
Task Score: 100%
Complexity: O(N*2)
"""
MAX_RETURN_VALUE = 10 ** 9


def solution(A):
    """
    This one is fairly easy and can be solved by using only two iterations:
    1. First go backwards and calculate the number of cars going west at any
        given point of the iteration
    2. Now going forward, we simple add the number of cars going west to the
        count if the car we encounter is travelling east.

    Warning:
         At the end, there is a mention to a max count of 1000 000 000 for the
         permutations. If this is exceeded the function should return -1.
    """
    # initialise variables to keep track of cars traveling west
    traveling_west = [0] * len(A)
    traveling_west_count = 0

    # do a reverse iteration to record the number of cars travelling west
    # at any given point of the iteration
    for i in reversed(range(len(A))):
        traveling_west_count += A[i]
        traveling_west[i] = traveling_west_count

    # now we do a normal iteration and calculate the permutations
    passing_cars_count = 0
    for idx, val in enumerate(A):

        # add permutations to count (only if car is travelling east)
        passing_cars_count += (1 - val) * traveling_west[idx]

        # check for max value
        if passing_cars_count > MAX_RETURN_VALUE:
            return -1

    return passing_cars_count
