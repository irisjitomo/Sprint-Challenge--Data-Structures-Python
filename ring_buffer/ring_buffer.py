from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # ring buffer sounds a lot like queue where the first one is
        # also the last one out so I just added to tail
        self.storage.add_to_tail(item)
        self.capacity += 1
        return self.capacity

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        # make a temp variable
        # if temp is less than storage length
        # grab head from storage
        # append self.storage.head.value to list_buffer_contents
        # increase temp += 1

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
