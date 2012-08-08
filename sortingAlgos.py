#!/usr/bin/env python


#####
#
# Merge sort implementation in python
#
###
import random
import time

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


class QuickSort:
    """
    Quicksort
    """
    def quickSort(self,list):
        if len(list) <= 1:
            return list
#        if len(list) > 1:
#            return self.quickSort(list)
#

        midPoint = len(list)/2
        mP = list[midPoint]
        sI=0
        eI=len(list) -1

        while sI < midPoint or midPoint < eI:
            #print 'Here'
            if list[sI] > mP > list[eI]:
                temp = list[sI]
                list[sI] = list[eI]
                list[eI] = temp
                sI +=1
                eI -=1

            elif list[sI] < mP > list[eI]:
                sI += 1

            elif list[sI] > mP < list[eI]:
                eI -= 1

            elif list[sI] < mP < list[eI]:
                sI += 1
                eI -= 1


            print sI,eI

        return list





if __name__ == '__main__':
    a = [i for i in range(10)]
    random.shuffle(a)
    t1 = time.time()
    #print BubbleSort().bubbleSort(a)
    t2 = time.time()
    print 'BubbleSort = ',(t2 - t1)

    random.shuffle(a)
    t1 =time.time()
    #print MergeSort().split(a)
    t2 = time.time()
    print 'MergeSort = ',(t2 - t1)


    random.shuffle(a)
    print a
    t1 =time.time()
    print QuickSort().quickSort(a)
    t2 = time.time()
    print 'QuickSort = ',(t2 - t1)
