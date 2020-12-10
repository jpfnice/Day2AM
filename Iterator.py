class Stack:
    def __init__(self, maxi=10):
        self.max = maxi
        self.data=[]
    def push(self, value):
        if len(self) < self.max:
            self.data.append(value)
        else:
            raise Exception("Stack is full")
    def pop(self):
        if len(self) > 0:
            return self.data.pop()
        else:
            raise Exception("Stack is empty")
    def __len__(self):
        return len(self.data)
    
    def __iter__(self):
        #return self.data.__iter__()
        self.n=len(self.data)-1
        return self
    
    def __next__(self):         
        if self.n >= 0:
            ix=self.n
            self.n -= 1
            return self.data[ix]
        else:
            raise StopIteration


p=Stack(5)
p.push(5)
p.push(8)
p.push(10)
p.push(12)
for e in p:
    print(e)
top=p.pop()
print(top)
for e in p:
    print(e)
    
    
    