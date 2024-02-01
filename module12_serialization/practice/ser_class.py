import pickle
from datetime import datetime
from time import sleep

class RememberAll:
    def __init__(self, *args):
        self.data = list(args)
        self.saved = None
        self.restored = None

    
    def __getstate__(self):
        state = self.__dict__.copy() # get all attributes as dictionary and copy them (copy state of instance of a class)
        state['saved'] = datetime.now()
        return state
    
    def __setstate__(self, state):
        self.__dict__.update(state)
        self.restored = datetime.now()

list_data = RememberAll(1,2,3)
print (list_data.data)

test_saving = pickle.dumps(list_data)
sleep(3)
loaded_data = pickle.loads(test_saving)
print(loaded_data.saved)
print(loaded_data.restored)
        