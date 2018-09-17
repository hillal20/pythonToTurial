class RingBuffer:
  def __init__(self, capacity):
    self.content = []
    self.capacity = capacity
   
    
  def append(self, item):
     if len(self.content) < self.capacity:
        self.content.append(item)
     elif len(self.content) == self.capacity:
        del(self.content[0])
        self.content.insert(0,item)
    elif len(self.content) > self.capacity:
        for i in self.content-self.capacity:
            del(self.content[0])
      
      self.content.insert(0,item)
    
  def get(self):
      print(self.content) 
 











buffer = RingBuffer(3)

buffer.append('a')
buffer.append('b')
buffer.append('c')

buffer.get()        # should return ['a', 'b', 'c']
buffer.append('d')  

buffer.get()        # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')

buffer.get()        # should return ['d', 'e', 'f']