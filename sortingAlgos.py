#!/usr/bin/env python


#####
#
# Merge sort implementation in python
#
###
import random
import time
import math

class MergeSort:
    """
    Divide the list into smaller sorted lists and then compare the elements of each list
    """

    def split(self,list):
        """
        Splits the list
        :param list:
        :return:
        """
        if len(list) <= 1:
            return list
        elif len > 1:
            left=list[:len(list)/2]
            right = list[len(list)/2:]
            left =  self.split(left)
            right = self.split(right)
            return self.merge(left,right)

    def merge(self,left,right):
        """
        Does the merge
        :param left:
        :param right:
        :return:
        """
        result=[]
        cl =0
        cr =0
        while len(left) > cl or len(right) > cr:
            if len(left)> cl and len(right) > cr:

                if left[cl] < right[cr]:
                    result.append(left[cl])
                    cl+=1
                else:
                    result.append(right[cr])
                    cr+=1
            elif len(left) > cl:
                result.append(left[cl])
                cl +=1
            elif len(right) > cr:
                result.append(right[cr])
                cr += 1
        return result


class InsertionSort:

    def insertionSort(self,list):
        for i in range(1,len(list)):
            j=i-1
            while j >= 0 and i>=1:
                if list[i] < list[j]:
                    temp = list[i]
                    list[i] = list[j]
                    list[j] = temp
                else:
                    break
                j-=1
                i-=1

        return list



class BubbleSort:

    def bubbleSort(self,list):

        for j in list:
#            #print list
#
            for i in list:
                if  i+1 < len(list):
                    if list[i+1] < list[i]:
                        temp = list[i+1]
                        list[i+1] = list[i]
                        list[i]=temp


        return list

class HeapSort:




    def heapSort(self,list):
        """

        :param endIndex:
        :param list:
        """

        endIndex = len(list)-1
        parentNode = (endIndex - 1)/2

        while parentNode >= 0:
            self.siftDown(parentNode,list,endIndex)
            parentNode -= 1

        self.swap(list,0,endIndex)
        endIndex -= 1
        while endIndex > 0:
            self.siftDown(0,list,endIndex)

            list[0],list[endIndex]=list[endIndex],list[0]
            endIndex -= 1



            #     print list
        return list

    def siftDown(self,node,list,endIndex):


        while node <= (endIndex -1)/2:
            child = 2 * node +1
            if child+1 <= endIndex and list[child+1] > list[child]:
                child+=1
            if list[child] > list[node]:
                list[child],list[node]=list[node],list[child]
                node = child
            else:
                return

       # return list



    def swap(self,list,id1,id2):
        list[id1],list[id2] = list[id2],list[id1]



    #def sort(self):

class QuickSort:
    """
    Quicksort : "Need to study more"
    """
    def quickSort(self,list):
        return self.qs(list,len(list),0)

    def qs(self,list,end,start):
        i=start
        k=end
        if end - start >1:
            mP = list[i]
            while k > i:
                while list[i] <= mP and i < end and k > i:
                    i+=1
                while list[k] >= mP and k >= start and k > i:
                    k -=1
                if k > i:
                    self.swap(list,i,k)



        else:
            return list

    def swap(self,list,i,k):
        temp = list[k]
        list[k] = list[i]
        list[i]= temp




if __name__ == '__main__':

    a = [i for i in range(100000)]
    random.shuffle(a)
    t1 = time.time()
    #print BubbleSort().bubbleSort(a)
    t2 = time.time()
    #print 'BubbleSort = ',(t2 - t1)

    random.shuffle(a)
    t1 =time.time()
    MergeSort().split(a)
    t2 = time.time()
    print 'MergeSort = ',(t2 - t1)


    random.shuffle(a)
    #print a
    t1 =time.time()
    #print QuickSort().quickSort(a)
    t2 = time.time()
    #print 'QuickSort = ',(t2 - t1)

    random.shuffle(a)
    t1 =time.time()
    HeapSort().heapSort(a)
    t2 = time.time()
    print 'HeapSort = ',(t2 - t1)
