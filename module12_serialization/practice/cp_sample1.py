from collections import UserList
from collections.abc import Iterable
from copy import copy, deepcopy

class GetElementLikeList(UserList):


    def __init__(self, data = []):
        self.data = data

    def __getitem__(self, key=None):
        if key is None:
            return self.data
        return self.data[key]
    
    def __len__(self):
        return len(self.data)
    
    def __add__(self, another: Iterable):
        self.data.extend(another.data)
        return self.data
    

    def __sub__(self, another):
        for i in another.data:
            if i in self.data:
                self.data.remove(i)
        return self.data
    
    def __lshift__(self, n):
        for _ in range(n):
            self.data.append(self.data.pop(0))
        return self.data
    
    def __rshift__(self, n):
        for _ in range(n):
            self.data.insert(0, self.data.pop())
        
        return self.data

