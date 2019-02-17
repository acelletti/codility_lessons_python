"""
Task Score: 100%
Complexity: O(N*log(N))
"""
MAX_RETURN_VALUE = 10 ** 7
START_POS = 0
END_POS = 1


def solution(A):
    """
    This one is a tricky one as the solution requires doing a bit of research on
    how to best detect overlapping ranges (a circle projected onto a axis
    becomes simply a range from A to B).

    The best performance can be achieved with the following approach:
    1. First pre-process all circles into a set starting points and endpoints.
    2. Sort the list of points by position, putting start points before
        endpoints.
    3. For each position we can now calculate how many open circles there are and
        count the intersection.

    Warning:
         At the end, there is a mention to a max count of 10 000 000 for the
         intersections. If this is exceeded the function should return -1.
    """
    # create representation of range for each circle
    circle_range = []
    for center, radius in enumerate(A):
        circle_range += [
            (center - radius, START_POS),
            (center + radius, END_POS)
        ]

    # we sort them by position first and edge type after (start before end)
    circle_range.sort()

    # counters for next iteration
    open_circles, intersections = 0, 0

    for _, edge_type in circle_range:
        if edge_type == START_POS:
            # we have reached the end of the previous position, add current open
            # circles to count
            intersections += open_circles

            # increase open circles count
            open_circles += 1
        else:
            # decrease open circles count
            open_circles -= 1

        # check for max value
        if intersections > MAX_RETURN_VALUE:
            return -1

    return intersections
