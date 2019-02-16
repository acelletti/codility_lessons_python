"""
Task Score: 100%
Complexity: O(1)
"""
import math


def solution(X, Y, D):
    """
    This is deceptively simple but quite devious.

    I have got to give it to the guys at codility here, the problem
    description implies a solution to the problem that is much more complex
    that is necessary. I am pretty sure that if implemented it using a while/for
    loop, this function would fail the performance mark by some degree.

    If we stop and think for a moment, the solution to this problem will
    smack us in the face. Who knew that paying attention in Maths classes could
    pay off?
    """
    # divide the distance by jump length
    return math.ceil((Y - X) / D)
