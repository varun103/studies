#!/usr/bin/env python

import random

class BubbleSort:

    def sort(self,array):
        for i in range(0,len(array)):

            for j in range(1,len(array)):
                if array[j] < array[j-1]:
                    array[j],array[j-1] = array[j-1],array[j]
                j+=1
            i+=1
        return array

    def __str__(self):
        return 'BubbleSort'

if __name__ == '__main__':
    pass