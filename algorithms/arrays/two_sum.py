"""
Two Sum - Hash Map Lookup

Idea:
    Scan the array once while storing seen values in a hash map.
    For each number, check if its complement has already appeared.

Complexity:
    Time: O(n) - single pass through the array
    Space: O(n) - hash map of seen values
"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:  # type: ignore
    seen = {}  # empty hash map

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i  # build hash map
