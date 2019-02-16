"""
Task Score: 100%
Complexity: O(N + M)
"""


def solution(N, A):
    """
    This problem took me a good while to solve. The problem in itself is not
    hard, but the description is not very clear. I had to read it several times
    and even then, it took me a good few tries until I realised what it was
    asking me to do.

    If I had been given this task in a ticket, in all honesty I probably would
    have contacted the owner directly to ask for clarification...

    Anyway I digress...

    The solution is fairly straightforward in itself: to get the time complexity
    down to the required level, simply keep track of the both the counter X
    and max counter while you iterate through A.

    After that we can flatten the counter list and return it.

    Complexity here would be O(len(A) + N)
    """
    # initialise variables to keep track of the counters
    counters = [0] * N
    counter_x, max_counter = 0, 0

    for val in A:
        # increase(X)
        if 1 <= val <= N:
            # increase counter X by 1
            counters[val - 1] = max(counters[val - 1], counter_x) + 1
            # update max counter
            max_counter = max(counters[val - 1], max_counter)

        # update counter to current max
        else:
            counter_x = max_counter

    # use list comprehension to re-calculate each counter
    return [max(val, counter_x) for val in counters]
