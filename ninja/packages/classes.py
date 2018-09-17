class Project:
  menu = {
    'tall':20,
    'short':10

  }

  def __init__(self, name, duration):
    self.name = name
    self.duration = duration

  def show(self):
      return self.menu['tall']