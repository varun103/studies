#!/usr/bin/env python

import logging

logging.basicConfig(level=logging.DEBUG)
class Node:
    """
    Represents a node in a 2-3-4 Tree
    """
    def __init__(self,elements=None,pointers=None):

        if not elements:
            self.keys = []
        else:
            self.keys = elements
        if not pointers:
            self.pointers=[]
        else:
            self.pointers = pointers
        self.parent = None

    def __repr__(self):
        return str(self.keys)


    def insert(self,key,pointers = None):
        """
        Inserts keys and pointers in a node
        :param key: the key to be added in the node
        :return: True if the key was successfully added
                False if the node if full
        """
        flag = True
        logging.debug('Inserting %s in %s' %(key,self) )

        if not self.keys:
            self.keys.append(key)
            if pointers:
                self.pointers.extend(pointers)
        elif len(self.keys) >= 3:
            logging.warn('Since node is full %s cannot be inserted in %s' %(key,self))
            return False
        else:
            flag = self.findPositionAndInsert(key,pointers)
        logging.debug('After inserting node = %s and pointers = %s' %(self,self.pointers))
        return flag


    def findPositionAndInsert(self,key,pointers=None):
        """
        Finds position of the new element in the node and inserts it
        If the new element has pointers associated with it includes them as well
                Changes the parent of the pointers to point to the current Node
        """
        position = self.findPosition(key)
        self.keys.insert(position,key)
        if pointers:
            self.pointers.insert(position,pointers[0])
            self.pointers.insert(position+1,pointers[1])
            pointers[0].parent = pointers[1].parent =self
        return True


    def findPosition(self,key):
        """
        Finds the positions of the new element in the node and returns it
        """
        position = 0
        while position < len(self.keys) and self.keys[position] < key:
            position+=1
        return position





class Tree:
    """
    Tree
    """

    def __init__(self):
        self.root=None


    def insert(self,key):
        """
        Inserts a key in the Tree
        :param key: the key to be added in the Tree
        """
        if not self.root:
            self.root = Node()
            self.root.insert(key)
        else:
            self.findAndInsert(self.root,key)



    def search(self,key):
        node = self.root




    def findNode(self,node,key):
        """
        Finds the node where the key should be inserted and returns the node
        :param node: The node to start searching from
        :param key: The key to be added
        :return:
        """
        logging.debug('Finding node for key %s ,current Node is %s'%(key,node))
        while node.pointers:
            logging.debug('looking in node %s with pointers %s' %(node,node.pointers))
            i =0
            while i < len(node.keys) and node.keys[i] < key :
                i +=1
            node =node.pointers[i]
        else:
            return node



    def merge(self,node,parent):
        """
        Merges the key with the parent
        """
        key = node.keys[0]
        inserted = parent.insert(key,node.pointers)
        if inserted:
            node.pointers[0].parent = node.pointers[1].parent = parent
        if not inserted:
            self.splitNode(parent,key,node)




    def splitNode(self,node,key,indNode=None):
        """
        Splits the node and returns the newly formed nodes and the
        :param node:
        :param key:
        :return:
        """

        #Node =[1,2,3]
        logging.debug('Splitting node %s' %node)
        #position=3
        position = node.findPosition(key)

        #new node = [1,2,3,4]
        node.keys.insert(position,key)

        if indNode:
            node.pointers.insert(position,indNode.pointers[0])
            node.pointers.insert(position+1,indNode.pointers[1])
            indNode.pointers[0].parent=indNode.pointers[1].parent=node


        newLeftNode = Node(elements=node.keys[:1],pointers=node.pointers[:2])
        for n in node.pointers[:2]:
            n.parent = newLeftNode
        newRightNode = Node(elements=node.keys[2:],pointers=node.pointers[2:])
        for n in node.pointers[2:]:
            n.parent = newRightNode

        newNode = Node(elements=node.keys[1:2],pointers=[newLeftNode,newRightNode])

        logging.info('New node is %s with pointers as %s' %(newNode,newNode.pointers))
        newLeftNode.parent= newRightNode.parent =newNode

        if node.parent:
            self.merge(newNode,node.parent)
            node.parent.pointers.remove(node)

        else:
            logging.debug('Node does not have a parent, creating new node')
            self.root = Node()
            self.merge(newNode,self.root)


    def findAndInsert(self,node, key):
        """
        Traverses the tree to look for the node where the key should be inserted
        and inserts it
        If the node exceeds the max number of elements it takes care of splitting the nodes as
        well
        :param node:
        :param key:
        :return:
        """
        leafNode = self.findNode(node,key)
        logging.debug('Key to be inserted in %s' %leafNode)
        inserted = leafNode.insert(key)
        if not inserted:
            self.splitNode(leafNode,key)


    def printNode(self,node):
        """
        Print through inline traversal
        """
        children = node.pointers
        keys = node.keys
        for count in range(len(children)):
            if children[count].pointers:
                self.printNode(children[count])
            else:
                for key in children[count].keys:
                    print key
            if not count == len(children)-1:
                print keys[count]


if __name__ == '__main__':
    t = Tree()
    for i in range(1,1001):
        t.insert(i)
    string=''
    t.printNode(t.root)
