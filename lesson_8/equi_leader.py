"""
Task Score: 100%
Complexity: O(N)
"""
import collections


def solution(A):
    """
    This problem is quite interesting and it is easily solved if we take into
    account that the leader of array A will be the only leader that is a valid
    candidate for equi leader indexes.

    Once we take this statement on board we can easily solve it:
    1. Find the leader of A and the number of occurrences.
    2. Create counters to record how many occurrences there are of the leader
        in both left and right split.
    3. Iterate through the array and record the movement of leaders only. For
        each index we then record whether it was an equi leader or not.
    """
    # get leader and number of occurrences for A
    leader, occurrences = collections.Counter(A).most_common(1)[0]

    # initialise counters for iteration
    equi_leader_count, l_leaders_count, r_leaders_count = 0, 0, occurrences

    for idx, val in enumerate(A):
        # value is leader, update counts
        if val == leader:
            l_leaders_count += 1
            r_leaders_count -= 1

        # index is equi leader, record it
        if l_leaders_count > (idx + 1) / 2 and \
                r_leaders_count > (len(A) - idx - 1) / 2:
            equi_leader_count += 1

    return equi_leader_count
