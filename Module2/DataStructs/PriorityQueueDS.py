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
