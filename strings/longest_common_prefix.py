"""
Longest Common Prefix - Chain Indexes

Idea:
    Compare characters at each position across all strings.
    Use nested loops: outer loop iterates through character positions,
    inner loop checks if all strings have the same character at that position.
    Stop when a mismatch is found or shortest string is exhausted.

Complexity:
    Time: O(n * m) where n is the number of strings and m is the length of the shortest string
    Space: O(1) excluding the output string

Returns:
    str: The longest common prefix shared by all strings, or empty string if non exists

Example:
    >>> longestCommonPrefix(["flower", "flow", "flight"])
    "fl"
    >>> longestCommonPrefix(["dog", "racercar", "car"])
    ""
"""


def longestCommonPrefix(strs: list[str]) -> str:
    common_prefix = ""
    shortest_len = min(len(s) for s in strs)

    for i in range(shortest_len):
        # Get the character from the FIRST string at position i
        current_char = strs[0][i]

        # Check if ALL other strings have the SAME character at position i
        for string in strs:
            if string[i] != current_char:
                return common_prefix

        # If we get here, all strings matched at position i
        # So we add this character to our prefix
        common_prefix += current_char

    return common_prefix
