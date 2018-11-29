##CS 2302 Data Structures
##Instructor:Diego Aguirre
##TA: Anindita Nath
##Project 5 Option B
##Modified and submitted by Andres Ponce 80518680
##Date of last modification 11/27/2018
##Purpose: Program creates a Min-Heap data structure
##from a given file with random numbers separated by a comma.
##Method of heapsort used to sort the min-heap.

import os
import random
import time
import re
import math

####################   Min-Heap    ######################

class Heap:
    def __init__(self):
        self.heap_array = []

    def insert(self,k):
        self.heap_array.append(k)
        #TODO: Complete implementation
        # percolate up from the last index to restore heap property.
        self.percolate_up(len(self.heap_array)-1)

    #Method used to insert new items into the min-heap and keep the property.    
    def percolate_up(self, node_index):
        while node_index > 0:
            # compute the parent node's index
            parent_index = (node_index - 1) // 2
            
            # check for a violation of the min heap property
            if not self.heap_array[node_index] <= self.heap_array[parent_index]:
                # no violation, so percolate up is done.
                return
            else:
                # swap heap_array[node_index] and heap_array[parent_index]
                temp = self.heap_array[node_index]
                self.heap_array[node_index] = self.heap_array[parent_index]
                self.heap_array[parent_index] = temp
                
                # continue the loop from the parent node
                node_index = parent_index
   #Method percolate_down used when an extraction is made to keep the min-heap property.             
    def percolate_down(self, node_index):
        child_index = 2 * node_index + 1
        value = self.heap_array[node_index]

        while child_index < len(self.heap_array):
            # Find the min among the node and all the node's children
            min_value = value
            min_index = -1
            i = 0
            while i < 2 and i + child_index < len(self.heap_array):
                if self.heap_array[i + child_index] < min_value:
                    min_value = self.heap_array[i + child_index]
                    min_index = i + child_index
                i = i + 1

            # check for a violation of the min heap property
            if min_value == value:
                return
            else:
                # swap heap_array[node_index] and heap_array[min_index]
                temp = self.heap_array[node_index]
                self.heap_array[node_index] = self.heap_array[min_index]
                self.heap_array[min_index] = temp
                
                # continue loop from the min index node
                node_index = min_index
                child_index = 2 * node_index + 1
                
    def extract_min(self):
        if self.is_empty():
            return None
        
        min_elem = self.heap_array[0]
        
        #TODO: Complete implementation
        #The largest element is poped and assigned to the first index
        #method percolate down is called to keep the min-heap properties.
        replacement = self.heap_array.pop()
        if len(self.heap_array) > 0:
            self.heap_array[0] = replacement
            self.percolate_down(0)
        return min_elem

    def is_empty(self):
        return len(self.heap_array)==0
    
#heap-sort method used to sort the min-heap array.
#it uses two loops to sort the array. 
def heap_sort(numbers):
    i = len(numbers) // 2 - 1
    #the first loop heapifies (converts the array into a heap)
    #the array using the min_heap_percolate_down.
    while i >= 0:
        min_heap_percolate_down(i, numbers, len(numbers))
        i = i - 1
                
    i = len(numbers) - 1
    #the second loop removes the minimum value, stores the value at the end,
    #and decrements the index until is zero
    while i > 0:
        # Swap numbers[0] and numbers[i]
        temp = numbers[0]
        numbers[0] = numbers[i]
        numbers[i] = temp

        min_heap_percolate_down(0, numbers, i)
        i = i - 1
#method used to sort the heap and percolate down the new added items.
def min_heap_percolate_down(node_index, heap_list, list_size):
        child_index = 2 * node_index + 1
        value = heap_list[node_index]

        while child_index < list_size:
            # Find the min among the node and all the node's children
            min_value = value
            min_index = -1
            i = 0
            while i < 2 and i + child_index < list_size:
                if heap_list[i + child_index] > min_value:
                    min_value = heap_list[i + child_index]
                    min_index = i + child_index
                i = i + 1
                                        
            if min_value == value:
                return

            # Swap heap_list[node_index] and heap_list[min_index]
            temp = heap_list[node_index]
            heap_list[node_index] = heap_list[min_index]
            heap_list[min_index] = temp
            
            node_index = min_index
            child_index = 2 * node_index + 1
            
#Creates a file of 20 random numbers separated by a comma
def createFile():
    newFile=open('listofnumbers.txt','w+')
    #Change the range and number of values
    numbers = random.sample(range(10000), 20)
    for item in numbers:
        newFile.write(str(item)+", ")
    newFile.close()

#Receives and reads the created file. Modifies the lines to create the heap
#and sort the min-heap. Extracts the minimum or first index and restore the
#min-heap property
def createHeap(file):
    h = Heap()
    for line in file:
        data = line.split()
    for item in data:
        item=int(item.strip(','))
        h.insert(item)
    print("Unsorted: ", h.heap_array)
    heap_sort(h.heap_array)
    print('Sorted: ', h.heap_array)
    print('Extraction: ', h.extract_min())
    print('Unsorted: ', h.heap_array)
    heap_sort(h.heap_array)
    print('Sorted: ', h.heap_array)
        
def main():
    createFile()
    newFile=open('listofnumbers.txt')
    createHeap(newFile)
main ()
