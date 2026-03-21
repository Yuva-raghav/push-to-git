class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode()
    tail = dummy
    
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    
    # Attach the remaining nodes
    tail.next = list1 if list1 else list2
    
    return dummy.next


# Example usage
# list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
