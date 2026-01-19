from data_structures.linked_lists import ListNode, build_list, print_list
from typing import Optional

l1 = [2, 4, 3]
l2 = [7, 0, 8]


def add_two_numbers(
    l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
    print("Starting with:", l1, l2)


if __name__ == "__main__":
    # Test inputs
    l1 = build_list([2, 4, 3])
    l2 = build_list([5, 6, 4])

    result = add_two_numbers(l1, l2)

    print_list(l1)
