"""
Task Score: 100%
Complexity: O(N)
"""


def solution(S):
    """
    This is super easy, no explanation needed.
    """
    # use counter to check nesting depth
    depth = 0

    for char in S:
        # increase depth
        if char == '(':
            depth += 1

        # decrease depth
        else:
            depth -= 1

            # negative depth is not allowed
            if depth < 0:
                return 0

    # return whether depth is 0
    return int(depth == 0)
