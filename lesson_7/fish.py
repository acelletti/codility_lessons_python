"""
Task Score: 100%
Complexity: O(N)
"""
import collections


def solution(A, B):
    """
    This problem is really simple, however I had to optimise my solution in
    order to get the necessary performance to achieve 100%.

    My initial solution removed the fish as it went along and it was
    marginally too slow for the judge in the sky that assigns the marks here.

    I re-implemented the same solution using a stack queue (FILO) as shown
    below:
    1. Iterate through the fish in the stream
    2. Every fish going downstream we push in the stack
    3. Every fish going upstream we pit against the stack. If it manages to
        eat all the fish in the stack, we count it as survived.
    4. At the end count how many survived and how many are left in the stack

    Note:
        The direction here is irrelevant and you could swap the
        upstream/downstream above and it would work (you would have to
        iterate backwards of course).

    """
    # create stack for fish going downstream (FILO)
    stack = collections.deque()

    # count fish that manage to swim to freedom upstream
    swam_to_freedom = 0

    for size, direction in zip(A, B):

        # fish going downstream, add it to the stack
        if direction == 1:
            stack.append(size)
        else:
            # pit fish against stack
            while len(stack):
                # big fish eat small fish
                if size > stack[-1]:
                    stack.pop()
                else:
                    break

            # no more fish to fight, fish has escaped
            if len(stack) == 0:
                swam_to_freedom += 1

    # count escaped from both sides
    return swam_to_freedom + len(stack)
