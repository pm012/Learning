"""implement LIFO using deque. Limit its size with the help
of constant MAX_LEN
function push adds value element to the beginning of the lifo list.
function pop extracts and returns first value from the list lifo
"""
from collections import deque

MAX_LEN =10

lifo = deque(maxlen=MAX_LEN)


def push(element):
    lifo.insert(0, element)
    


def pop():
    return lifo.popleft()