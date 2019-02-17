"""
Task Score: 100%
Complexity: O(N)
"""
import collections

OPEN_BRACKETS = ["{", "[", "("]
BRACKETS_DICT = {"}": "{", "]": "[", ")": "("}


def solution(S):
    """
    This problem sounds like its asking us to build a rudimentary interpreter:
    all it asks is that we keep track of open and closed brackets.

    The approach is as follows:
    1. Create a stack (FILO queue)
    2. For each open bracket push it on the stack, while for each closed one
        either pop it from the stack or terminate if not found
    3. Once finished, we can check the stack and if empty, the string is
        balanced.

    Note:
        I have used a deque object as it is specifically optimised for FIFO &
        FILO queues (appending & popping either end is extremely fast).
        I have checked, out of curiosity, and it looks like this code still gets
        100% if we use a simple list as a stack.

    """
    # create stack as FILO queue
    stack = collections.deque()

    for char in S:
        # open brackets, pop it on the stack
        if char in OPEN_BRACKETS:
            stack.append(char)
        else:
            # get matching open bracket
            open_bracket = BRACKETS_DICT[char]

            # if its not on the stack, stop here
            if len(stack) < 1 or stack[-1] != open_bracket:
                return 0

            # pop it from the stack
            stack.pop()

    # return whether the stack is empty or not
    return int(len(stack) == 0)
