from collections import deque
class MovingAverage:
  
  def __init__ (self, size):
    #self.datastream = [] * size
    self.datastream = deque(maxlen=size)

  def next(self, val):
    self.datastream.append(val)
    count = 0
    for d in self.datastream:
      if d != None:
        count+=1
    avg = sum(self.datastream)/float(len(self.datastream))
      
    return avg


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

ma = MovingAverage(3);
ma.next(1) 

print(ma.next(3) )
print(ma.next(5) )
print(ma.next(3) )
print(ma.next(21) )
