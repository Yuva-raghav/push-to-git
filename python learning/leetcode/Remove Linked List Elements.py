class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_elements(head: ListNode, val: int) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    current = dummy

    while current.next:
        if current.next.val == val:
            current.next = current.next.next
        else:
            current = current.next

    return dummy.next


# Example usage:
# Build linked list: 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6
head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))

new_head = remove_elements(head, 6)

# Print result: should be 1 -> 2 -> 3 -> 4 -> 5
while new_head:
    print(new_head.val, end=" -> " if new_head.next else "")
    new_head = new_head.next
