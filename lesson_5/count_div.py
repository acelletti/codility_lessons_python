"""
Task Score: 100%
Complexity: O(1)
"""
import math


def solution(A, B, K):
    """
    While the previous problem was mathematically challenging, this one is a
    doodle.
    """
    return math.floor(B / K) - math.ceil(A / K) + 1

