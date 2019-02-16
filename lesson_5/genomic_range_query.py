"""
Task Score: 100%
Complexity: O(N + M)
"""

MINIMUM_IMPACT_RESULT = [
    ('A', 1),
    ('C', 2),
    ('G', 3),
    ('T', 4)
]


def get_minimum_impact_factor(last_position_of, start, end):
    # find minimum impact factor
    for letter, return_value in MINIMUM_IMPACT_RESULT:
        if last_position_of[letter][end] >= start:
            return return_value

    # this should never happen
    assert False, "Something went wrong with the application logic."


def solution(S, P, Q):
    """
    The problem asks us to find the minimum impact factor given a set of
    lower and upper bounds on a DNA string.

    The approach is as follows:
    1. Make a record of the last position a certain letter was seen for each
        index in the string.
    2. For each set of lower/upper bounds, find the minimum factor by looking
        at the last position seen in ascending order (smaller to bigger)
    3. Aggregate the result into a list and return it.

    """
    # dictionary to record last position for DNA letters
    last_position_of = {
        'A': [-1] * len(S),
        'C': [-1] * len(S),
        'G': [-1] * len(S),
        'T': [-1] * len(S)
    }

    # populate records
    for i in range(len(S)):
        for letter in last_position_of.keys():
            # letter found, set as current idx
            if S[i] == letter:
                last_position_of[letter][i] = i
            # copy the previous value
            elif i > 0:
                last_position_of[letter][i] = last_position_of[letter][i - 1]

    # return list if minim impact factors
    return [get_minimum_impact_factor(last_position_of, start, end)
            for start, end in zip(P, Q)]
