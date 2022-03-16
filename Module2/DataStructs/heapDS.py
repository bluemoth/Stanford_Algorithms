# to do - finish implmenetaiton of custom heap DS inheriting from priority queue DS

import PriorityQueueDS


class HeapPriorityQueue(PriorityQueueDS):
    '''Min priority queue implemented with binary heap'''

    def _parent(self, j):
        return (j-1)//2 # parent formula is (index-1)/2 which helps build the 