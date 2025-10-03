"""
Завдання 1. Структури даних. Сортування. Робота з однозв'язним списком
Для реалізації однозв'язного списку (приклад реалізації можна взяти з конспекту) необхідно:

    - написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
    - розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
    - написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список.
"""

import copy


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __lt__(self, other):
        return self.data < other.data

    def __le__(self, other):
        return self.data <= other.data


class LinkedList:
    def __init__(self):
        self.head = None

    def __len__(self):
        size = 0
        current = self.head
        while current:
            size += 1
            current = current.next

        return size

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse(self):
        prev = None
        cur = copy.copy(self.head)
        next = cur.next

        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        self.head = prev

    def sort(self):
        self.head = LinkedList.merge_sort(self.head)

    def splice(self, llist, inplace=True):
        dummy = Node()
        current_spliced = dummy
        current_1 = self.head
        current_2 = llist.head

        while current_1 and current_2:
            if current_2 < current_1:
                current_spliced.next = current_2
                current_2 = current_2.next
            elif current_1 < current_2:
                current_spliced.next = current_1
                current_1 = current_1.next
            current_spliced = current_spliced.next

        current_spliced.next = current_1 if current_1 else current_2

        if inplace == True:
            self.head = dummy.next
            return self.head

        result = LinkedList()
        result.head = dummy.next
        return self.head

    @classmethod
    def merge(cls, left, right):
        dummy = Node()
        tail = dummy
        while left and right:
            if left.data <= right.data:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        tail.next = left if left else right
        return dummy.next

    @classmethod
    def merge_sort(cls, head):
        if head is None or head.next is None:
            return head

        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        left = cls.merge_sort(head)
        right = cls.merge_sort(mid)
        return cls.merge(left, right)


llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

# Друк зв'язного списку
print("Зв'язний список:")
llist.print_list()

# Розвертаємо зв'язний список
llist.reverse()
print("Реверсований зв'язний список:")
llist.print_list()

# Сортуємо зв'язний список
llist.sort()
print("Сортований список:")
llist.print_list()

# Створюємо другий список
llist2 = LinkedList()
llist2.insert_at_end(6)
llist2.insert_at_end(16)
llist2.insert_at_end(30)

# Об'єднуємо 2 списки
llist.splice(llist2)
print("Об'єдниний зв'язний список:")
llist.print_list()
