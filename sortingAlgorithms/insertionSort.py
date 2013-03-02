#!/usr/bin/env python

class InsertionSort:

    def sort(self,array):

        for i in range(0,len(array)):
            for j in range(i+1,len(array)):
                if array[j] < array[i]: array[j],array[i]=array[i],array[j]
        return array


    def __str__(self):
        return 'Insertion Sort'