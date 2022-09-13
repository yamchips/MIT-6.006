from hashlib import new


class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        new_node = Doubly_Linked_List_Node(x)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_last(self, x):
        new_node = Doubly_Linked_List_Node(x)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def delete_first(self):
        assert self.head
        x = self.head.item
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None        
        return x

    def delete_last(self):
        assert self.tail
        x = self.tail.item
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        return x

    def remove(self, x1, x2):
        L2 = Doubly_Linked_List_Seq()
        L2.head = x1
        L2.tail = x2
        if self.head == x1:
            self.head = x2.next
        else:
            x1.prev.next = x2.next

        if self.tail == x2:
            self.tail = x1.prev
        else:
            x2.next.prev = x1.prev
        x1.prev = None
        x2.next = None
        return L2

    def splice(self, x, L2):
        x1 = L2.head
        x2 = L2.tail
        x3 = x.next
        L2.head = None
        L2.tail = None
        x1.prev = x
        x.next = x1
        x2.next = x3
        if x == self.tail:
            self.tail = x2
        else:        
            x3.prev = x2
