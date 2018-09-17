import functools
class TemperatureTracker:
  #  Write a class TempTracker that tracks the max, min, mean,
  #  and mode of temperature values as they are inserted into
  #  the TempTracker. This class should have the following methods:

  def __init__(self):
    self.degrees = [] 
    self.max = 0
    self.min = 0
    self.mean = 0
    self.mode = 'natural'

  
  def insert(self, temp):
      self.degrees.append(temp)
      return self.degrees
  
  def get_max(self):
      m = max(self.degrees)
      self.max = m 
      return self.max
  
  def get_min(self):
     mn = min(self.degrees)
     self.min = mn 
     return self.mins
  
  def get_mean(self):
      def add(x,y):
          y = y + x 
          return y 
      total = functools.reduce(self.degrees, add)
      l = len(self.degrees)
      mean = float(total/l)
      self.mean = mean 
      return self.mean 
    
  
  def get_mode(self):
      modes = [ self.degrees.count(i) for i in self.degrees]
      