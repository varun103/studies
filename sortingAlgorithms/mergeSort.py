#!/usr/bin/env python



class MergeSort:

    def sort(self,array):

        if len(array) <= 1:
            return array
        else:
            left = self.sort(array[:(len(array) / 2)])
            right = self.sort(array[(len(array) / 2):])
            array = self._merge(left,right)
        return array

    def _merge(self,left,right):
        array =[]
        i=0
        j=0
        while i < len(right) and j < len(left) :
            if left[j] < right[i]:
                array.append(left[j])
                j += 1
            else:
                array.append(right[i])
                i += 1
        if i < len(right):
            array.extend(right[i:])
        elif j < len(left):
            array.extend(left[j:])
        return array

    def __str__(self):
        return 'MergeSort'



