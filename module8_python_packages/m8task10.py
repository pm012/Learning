"""
implement FIFO using deque. Limit its size with the help
of constant MAX_LEN
function push adds value element to the beginning of the fifo list.
function pop extracts and returns first value from the list lifo
"""
from collections import deque

MAX_LEN =10

fifo = deque(maxlen=MAX_LEN)


def push(element):           
    return fifo.insert(len(fifo),element)
    


def pop():
    return fifo.popleft()


for i in range(1,10):
    push(i)

print(fifo)

print(pop())
print(fifo)