class Bill:
  def __init__(self, name):
     self.name = name

  @property 
  def showName(self):
      return self.name
  
  @showName.setter
  def showName(self,name):
      self.name = name 

hill = Bill('hilal')

hill.showName = 'bilal'
print(hill.name )
print(hill.showName)
############################################## setters && getters

