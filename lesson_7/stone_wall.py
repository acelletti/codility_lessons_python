"""
Task Score: 100%
Complexity: O(N)
"""
import collections


def solution(H):
    """
    It seems that lesson 7 is mostly about stack queues and this one does not
    disappoint.

    The solution here is a bit complex but I will do my best to explain:
    1. Create the stack where to store the block sizes (FILO queue)
    2. For each height, get rid of all the blocks in the stack that are
        taller than the current one.
    3. Once done, if the block on top of the stack is smaller, we add a new
        one with the current height.
    4. At the end, we simply count how many blocks we added.

    """
    # create stack for fish going downstream (FILO)
    stack = collections.deque()

    # count the number of blocks
    n_blocks = 0

    for height in H:
        # remove all blocks taller than current
        while len(stack) and height < stack[-1]:
            stack.pop()

        # if there are no blocks in the stack or the
        # last block is not of required height
        # add a new block
        if len(stack) == 0 or height != stack[-1]:
            stack.append(height)

            # record block for result
            n_blocks += 1

    return n_blocks

