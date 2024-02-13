class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_linked_list(head):
        current = head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

list1 = ListNode(1, ListNode(3, ListNode(5)))
list2 = ListNode(2, ListNode(4, ListNode(6)))



# Выводим результат
print("List 1:")
print_linked_list(list1)

print("List 2:")
print_linked_list(list2)