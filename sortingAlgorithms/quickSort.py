#!/usr/bin/env python

"""
Algorithm :

Quicksort -> Given a list of n integers, select a number as the pivot(ial) number and then
divide up the other numbers into two list either, where the list to the left contains numbers

"""





class QuickSort:

    def sort(self,array):
        left = []
        right = []
        pivotList = []

        if len(array) <= 1:
            return array
        else:
            pivot = array[0]
            for i in array:
                if i < pivot:
                    left.append(i)
                elif i > pivot:
                    right.append(i)
                else:
                    pivotList.append(i)
            left=self.sort(left)
            right=self.sort(right)
            return left + pivotList + right


    def __str__(self):
        return 'QuickSort'