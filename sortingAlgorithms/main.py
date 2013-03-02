#!/usr/bin/env python

import random
import time
from bubbleSort import BubbleSort
from quickSort import QuickSort
from insertionSort import InsertionSort
from mergeSort import MergeSort

def sort(sortObj):
    array = [i for i in range(1,10)]
    random.shuffle(array)
    print "Before =" + str(array)
    startTime = time.time()
    array = sortObj.sort(array)
    endTime = time.time()
    print "After %s = %s" %(str(sortObj) ,str(array))
    print "TimeTaken = %f\n" %((endTime - startTime)*1000)


sortinAlgoObjects = [QuickSort(),InsertionSort(),BubbleSort(),MergeSort()]
for sortingObjects in sortinAlgoObjects:
    sort(sortingObjects)





