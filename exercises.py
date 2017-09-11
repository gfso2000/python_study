'''
Created on Dec 12, 2016

@author: I325639
'''
from _collections import deque
import heapq

portfolio=[
   {'name':'IBM','shares':100,'price':91.1},
   {'name':'Oracle','shares':100,'price':54.3},
   {'name':'HP','shares':100,'price':21.03},
   {'name':'SAP','shares':100,'price':31},
]

print(heapq.nlargest(2, portfolio, lambda s:s['price']))
