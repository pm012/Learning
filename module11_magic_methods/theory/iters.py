class MyIterator:
    def __init__(self, seq, stop=1):
        self.seq = seq
        self.stop = stop
        self.loop = 0
        self.idx = 0


    def __iter__(self):
        return self
    
    def __next__(self):
        if self.loop >= self.stop:
            raise StopIteration
        else:
            value = self.seq[self.idx]
            self.idx += 1
            if self.idx == len(self.seq):
                self.idx = 0
                self.loop += 1
            return value
        
seq = ['qwe', 'rty','none', 3,7, True]

my_iterator = MyIterator(seq, 2)
for val in my_iterator:
    print(val)