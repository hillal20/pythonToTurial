

class Node:

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, item):
        node = Node(item)
        current = self.head
        while current.get_next() != None:
            current = current.get_next()
        current.set_next(node)

    # """Returns the number of nodes in the linked list"""
    def size(self):
        if self.head == None:
            return 0
        current = self.head
        count = 1
        while current.get_next() != None:
            count += 1
            current = current.get_next()
        return count

    def search(self, target):
        current = self.head
        if current.get_data() == target:
            return current
        while current.get_next() != None:
            current = current.get_next()
            if current.get_data() == target:
                return current
        return None

    def delete(self, target):
        current = self.head
        previous = None

        while True:

            if current.get_data() == target:
                if previous:
                    previous.get_next(current.get_next())
                else:
                    self.head = current.get_next()
                return True

            previous = current
            current = current.get_next()
        return False
