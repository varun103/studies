
import random

class Node:
    """
    NODE class
    """
    rChild,lChild,parent,data = None,None,None,0

    def __init__(self,key):
        self.rChild = None
        self.lChild = None
        self.parent = None
        self.data = key

class Tree:

    root,size = None,0
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self,number):
        """
        Inserts elements into the tree
        :param number:
        :return:
        """

        if self.root is None:
            self.root = Node(number)
            self.root.parent = None

        else:
            self._insertWithNode(self.root,number)





    def search(self,number):
        """
        search for an element in a binary search tree

        :param number:
        :return: True if found
        """
        return self._searchWithRoot(self.root,number)

    def minimum(self,root=None):
        """
        Finds the minimum in the search tree
        :return:
        """
        if not root:
            root = self.root
        while root.lChild is not None:
            root = root.lChild
        return root

    def maximum(self):
        """
        Returns the max element in the tree
        :return:
        """
        root= self.root
        while root.rChild is not None:  root= root.rChild
        return root.data


    def delete(self,number):
        node = self.search(number)
        print node.__dict__
        if node:
            if node.lChild is None and node.rChild is None:
                parent = node.parent

                if node ==  parent.rChild: parent.rChild = None
                else :  parent.lChild = None


            elif node.lChild is None or node.rChild is None:
                print 'Case 2'
                if node.lChild: child = node.lChild
                else:   child = node.rChild
                parent = node.parent
                if parent:
                    if parent.rChild == node:
                        parent.rChild = child
                    else:   parent.lChild = child
                    child.parent = parent
                else:
                    child.parent = None
                node = None

            else:
                print 'Case 3'
                rTreeRoot = node.rChild

                min = self.minimum(rTreeRoot)
                minParent = min.parent
                min.lChild = node.lChild

                if node.rChild != min:
                    min.rChild = node.rChild
                    if min == minParent.lChild:
                        minParent.lChild =None
                    else:   minParent.rChild= None

                parent = node.parent

                if parent:
                    if parent.rChild == node:
                        parent.rChild = min
                    else:
                        parent.lChild = min
                else:
                    min.parent = None

                node = None


    def createCopy(self):
        root = self.root

        new = Tree()
        


    def preOrderTraverse(self,root):
        """
        Prints the tree starting with the root first and then the children
        :param root:
        :return:
        """
        if root is None:
            return
        else:
            print root.data
            self.preOrderTraverse(root.lChild)
            self.preOrderTraverse(root.rChild)


    def inOrderTraverse(self,root):
        """
        Prints the tree starting with the child -> root -> child
        :param root:
        :return:
        """
        if root is None:
            return
        else:
            self.inOrderTraverse(root.lChild)
            print root.data
            self.inOrderTraverse(root.rChild)


    def postOrderTraverse(self,root):
        """
        Prints the tree with children first and root as the last element
        :param root:
        :return:
        """
        if root is None:
            return
        else:
            self.postOrderTraverse(root.lChild)
            self.postOrderTraverse(root.rChild)
            print root.data

    def printTree(self,someNode):
        """
        Prints the tree inorder
        :param someNode:
        :return:
        """
        if someNode is None:
            pass
        else:
            self.printTree(someNode.lChild)
            print someNode.data
            self.printTree(someNode.rChild)

    def findCommonAncestor(self,node1,node2):
        pass


    #Internals

    def _searchWithRoot(self,root,number):
        if number < root.data and root.lChild:
            return self._searchWithRoot(root.lChild,number)
        elif number > root.data and root.rChild:
            return self._searchWithRoot(root.rChild,number)
        elif number == root.data:
            return root
        else:   return False



    def _iterativeSearch(self,root,number):

        while root.data is not number and root is not None:
            if number < root.data:
                root = root.lChild
            elif number > root.data:
                root = root.rChild

        if number == root.data:
            return root
        elif root is None:
            return 'Not Found'


    def _insertWithNode(self,root,number):
        if root.rChild is None and root.lChild is None:

            if number >= root.data:
                node= Node(number)
                root.rChild = node
                node.parent = root
            elif number < root.data:
                node = Node(number)
                root.lChild = node
                node.parent = root


        elif number >= root.data:
            if root.rChild is None:
                node = Node(number)
                root.rChild = node
                node.parent = root
            else:
                root = root.rChild
                self._insertWithNode(root,number)

        elif number < root.data:
            if root.lChild is None:
                node = Node(number)
                root.lChild = node
                node.parent = root
            else:
                root = root.lChild
                self._insertWithNode(root,number)


def main():
    t = Tree()
    a = [10,5,30,2,7,20,40,35,100,110]
#    a = [i for i in range(20,100)]
#    random.shuffle(a)
#    #print a
    for i in a:
        t.insert(i)

#    t.insert(10)

    #print t.maximum()
    t.delete(30)

    t.inOrderTraverse(t.root)

if __name__ == '__main__':
    main()