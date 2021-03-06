
class Linkedlist(object):
    def __init__(self, value):
        self.value     = value
        self.prev_node = None
        self.nxt_node  = None
        print 'initialized node', self

    def insert_last(self, last_node):
        if last_node:
            last_node.nxt_node = self
            self.prev_node = last_node
            print 'this node',self,'added after last_node',self.prev_node
        else:
            print 'this node',self, 'added from empty'

    def delete(self):
        if self.nxt_node and self.prev_node:
            self.nxt_node.prev_node = self.prev_node
            self.prev_node.nxt_node = self.nxt_node
            print 'deleted node', self, 'between prev', self.prev_node, 'and next', self.nxt_node
        elif self.nxt_node:
            self.nxt_node.prev_node = None
            print 'deleted node', self, 'before nxt', self.nxt_node
        elif self.previous_node:
            self.prev_node.nxt_node = None
            print 'deleted node', self, 'nextto prev', self.prev_node
        else:
            pass

        self.prev_node = None
        self.nxt_node = None
        print 'finished deletion', self

    def insert_between(self, prev, nxt):
        print  self, 'insert between', prev, 'and', nxt
        prev.nxt_node = self
        self.prev_node = prev
        nxt.prev_node = self
        self.nxt_node = nxt
        print 'inserted node', self, 'between prev', self.prev_node, 'and next', self.nxt_node

    def __show__(self):
        return self.value

    def __unicode__(self):
        return self.value

    def __repr__(self):
        return self.value

    def show(self):
        print self.prev_node, '- ', self, '-',self.nxt_node

    def show_prev(self):
        print 'SHOW PREV',self
        if self.prev_node:
            self.prev_node.show_prev()

    def show_nxt(self):
        print 'SHOW NXT',self
        if self.nxt_node:
            self.nxt_node.show_prev()

elem_1 = Linkedlist('element_1')
elem_2 = Linkedlist('element_2')
elem_3 = Linkedlist('element_3')
elem_4 = Linkedlist('element_4')
elem_5 = Linkedlist('element_5')
elem_6 = Linkedlist('element_6')


# add node from empty
elem_1.insert_last(None)
elem_1.show()
print "-" * 10
elem_2.insert_last(elem_1)
elem_2.show()
elem_2.prev_node.show()
print "-" * 10
elem_3.insert_last(elem_2)
elem_3.show()
elem_3.prev_node.show()
elem_3.prev_node.prev_node.show()
elem_1.nxt_node.show()
elem_1.nxt_node.nxt_node.show()
elem_2.show()
elem_2.prev_node.show()
elem_2.nxt_node.show()
print "-" * 10
elem_4.insert_between(elem_1,elem_2)
elem_4.show()
elem_4.nxt_node.show()
elem_4.nxt_node.nxt_node.show()
print "-" * 10
elem_2.delete()
elem_2.show()
elem_1.show()
elem_3.show()
elem_4.show()

