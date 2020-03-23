import numpy as np

class Node():
    def __init__(self, val):
        self.val = val
        self.next = None


    def traverse(self):
        node = self #start from the head node
        while node != None:
            print(node.val) #access the node value
            node = node.next #move on to the next node



class DoublyNode():
    def __init__(self, val):
        self.val = data
        self.next = None
        self.prev = None
