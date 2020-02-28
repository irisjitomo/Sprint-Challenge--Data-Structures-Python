from doubly_linked_list import DoublyLinkedList

from doubly_linked_list import ListNode


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
            # checks to see if self.storage
        while self.storage: 
            # set current node to self.storage.head
            self.current = self.storage.head 
            # insert item to linked list
            self.storage.add_to_head(item)
            self.current = self.storage.head.next
            # if capacity is reached 
            if self.storage > self.capacity:
                # remove current head node
                self.storage.remove_from_head(self.current)
                # add_to_head the item
                self.storage.add_to_head(item)
                # set current node to head.next
                # self.current = self.storage.head.next

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
