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
        while self.storage.length < self.capacity: 
            # insert item to linked list
            self.storage.add_to_head(item)
            self.current = self.storage.head.next

            if self.storage.length == self.capacity and self.current == self.storage.tail:
                # remove current head node
                self.storage.remove_from_tail()
                # add_to_head the item
                self.storage.add_to_tail(item)
                self.current = self.storage.head

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

