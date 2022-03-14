'''
Purpose of this .py file is to manually draft a priority queue (heap) data structure from scratch.

Important points regarding priority queue:


'''

class PriorityQueueBase:
    '''Abstract class for priority queue base'''


    class item:
        '''store items'''
        __slots__ = '_key', '_value'

        def __init__(self,k,v):
            self._key = k
            self._value = v

        def __str__(self):
            '''String method to help desriibe print(class)'''
            return f'key: {self._key}, value: {self._value}'

        def is_empty(self):
            '''Returns true if empty'''
            return len(self) == 0

        def __lt__(self, other):
            '''Less than'''
            return self._key < other._key


'''Need to incorporate sorted and unsorted pqs, along with possible locater for adaptable PQ (use in Dijkstra)'''

# example declaration of pq item
pq1 = PriorityQueueBase.item(1,2)
print(pq1)

pq2 = PriorityQueueBase.item(3,4)
print(pq2)

print(pq1 > pq2)
