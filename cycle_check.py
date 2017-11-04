"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
"""
class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node



def has_cycle(head):
    if(head is None):
        return 0
    else:
        marker1 = head
        marker2 = head

        while marker2 != None and marker2.next != None:
            marker1 = marker1.next
            marker2 = marker2.next.next
            
            if marker1.data == marker2.data:
                return 1
        return 0
        