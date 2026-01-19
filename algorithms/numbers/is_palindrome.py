"""
Palindrome Number - Reverse Half Method

Idea:
    Reverse only the second half of digits and compare to first half.
    Stop when reversed_half >= x (half the digits processed).

Complexity:
    Time: O(log n) - proportional to number of digits
    Space: O(1) - constant space
"""


def is_palindrome(x: int) -> bool:
    # Negative numbers aren't palindromes
    if x < 0:
        return False

    # Numbers ending in 0 can't be palindromes (except 0 itself)
    if x != 0 and x % 10 == 0:
        return False

    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10  # Build the reversed second half
        x //= 10

    # Even length | Odd length (ignore middle digit)
    return x == reversed_half or x == reversed_half // 10
