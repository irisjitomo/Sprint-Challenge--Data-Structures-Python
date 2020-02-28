from doubly_linked_list import DoublyLinkedList

from doubly_linked_list import ListNode


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
            # checks to see if self.storage
            # set current node to self.storage.head 
        if self.current == None:
            self.current = self.storage.head
        if self.storage.length < self.capacity: 
            # insert item to linked list
            self.storage.add_to_tail(item)
            # self.current = self.storage.head.next

        elif self.storage.length == self.capacity:
            # remove current head node
            removed_head = self.storage.head
            self.storage.remove_from_head()
            # add_to_head the item
            self.storage.add_to_tail(item)
            if removed_head == self.current:
                self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        current = self.current
        list_buffer_contents.append(current.value)
        if current.next:
            node = current.next
        else:
            node = self.storage.head
        while node is not current:
            list_buffer_contents.append(node.value)
            if node.next:
                node = node.next
            else:
                node = self.storage.head

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass

