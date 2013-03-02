#!/usr/bin/env python




class Heap:

    def __init__(self):
        self.top

    def heapify(self,value):
        if not self.top:
            self.top=Node(None,None,value)
        elif value < self.top.value:
            pass #traverse left
        elif value > self.top.value:
            pass #traverse right


class Node:

    def __init__(self,right,left,value):
        self.rightChild=right
        self.leftChild = left
        self.value = value



def heapify():
    pass
