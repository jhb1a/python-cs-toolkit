from typing import Optional


class ListNode:
    """
    Node of a singly linked list.

    Attributes:
        val: The integer value stored in the node.
        next: Reference to the next ListNode in the chain.

    Example:
        head -> [2]
                [3]
                [4] <- curr
    """

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def build_list(values: list[int]) -> Optional[ListNode]:
    """
    Build a linked list from a Python list of integers.

    Args:
        values: List of integers.

    Returns:
        Head of the constructed linked list.
    """
    if not values:
        return None

    head = curr = ListNode(values[0])
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


def to_list(head: Optional[ListNode]) -> list[int]:
    """
    Convert a linked list back into a Python list.

    Args:
        head: Head of a linked list.

    Returns:
        List of integers representing the linked list.
    """
    out = []
    curr = head
    while curr:
        out.append(curr.val)
        curr = curr.next
    return out


def print_list(head: Optional[ListNode]) -> None:
    """
    Print a linked list in a readable arrow format.

    Example:
        2 -> 4 -> 3
    """
    vals = []
    curr = head
    while curr:
        vals.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(vals) if vals else "Empty list")


def LL(values: list[int]) -> Optional[ListNode]:
    """
    Short-hand builder for quick testing.

    Example:
        l1 = LL([2,4,3])
    """
    return build_list(values)
