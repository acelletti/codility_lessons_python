"""
Task Score: 100%
Complexity: O(N * log(N))
"""
import collections


def solution(A):
    """
    This can be easily implemented by taking advantage of the
    collections.Counter object.

    Warning:
        Be careful in reading the description of the problem as at the beginning
        it mentions that the element is unpaired (which I take to mean count=1).
        However in the assumptions at the bottom, it then mentions that the
        element that we are looking for occurs an odd amount of times.

    What we need to do is:
    1. Use the counter to get the values and their count in the list
    2. Iterate through the counter to find the element with an odd number of
        occurrences.

    I also like to be a nice guy and handle the case where said element is
    not found, in this case we raise an exception since the assumptions made
    by this function are quite clear and therefore the input is invalid.

    If we were writing this function for real, I personally would have returned
    None as this is a more elegant way of handling the case where there is no
    element to return.
    """

    # get counter for array
    counter = collections.Counter(A)

    # initialise counters
    for value, count in counter.items():

        # odd one found, return it
        if count % 2 > 0:
            return value

    # value not found
    raise ValueError("The array A does not contain any values "
                     "that occur an odd number of times.")
