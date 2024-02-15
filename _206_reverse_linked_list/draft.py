# Создание тестовых данных
# 1 -> 2 -> 3 -> 4 -> 5 -> None
from _206_reverse_linked_list.solution_1 import Solution, ListNode

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Печать исходного списка
print("Исходный список:")
current_node = head
while current_node:
    print(current_node.val, end=" -> ")
    current_node = current_node.next
print("None")

# Создание экземпляра класса Solution
solution = Solution()

# Запуск метода reverseList и печать результата
reversed_head = solution.reverseList(head)

# Печать развернутого списка
print("Развернутый список:")
current_node = reversed_head
while current_node:
    print(current_node.val, end=" -> ")
    current_node = current_node.next
print("None")