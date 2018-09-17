class Build:
  def __init__(self, name , age , city):
    self.name = name
    self.age = age 
    self.city = city 
  # def __str__(self):
  #     return str({self.name,self.age,self.city})

  def __repr__(self):
        return "<Human: %s, %d>" % (self.name, self.age)



class Hill(Build):
  def __init__(self,name,age,city, team, Class):
     super().__init__(name,age,city)
     self.team = team 
     self.Class = Class
  # def __str__(self):
  #     return str({self.Class,self.team})
  # def __repr__(self):
  #       return "<Human: %s, %d>" % (self.name, self.age)

a = Build("hillal", 33,'nyc')
print(a)
b = Hill("fill", 35,'nj', 'barca', 'cs9')

print(b)