# name = input('===> tell me your name: ');
# age = float(input("=== tell me your age: "))

# print('name===> ',name);
# print('age===> ',age);

# print(f"name:{name}")
# print(f'age:{age:.4}')

# bill = ['fill','hill','dill','gill']
# for i in bill[1:3]:
#  print(i)
###############3333
# num = 0

# while True:
#   if num == 11:
#     break
#   print(num)
#   num += 1
##############
# for i in range(0,20,4):
#   print(i)
####################
# cities = ['villa', 'nyc', 'nj', 'al', 'cal', 'miami']
# for i in range(len(cities)-1,-1,-1):
#   print(f"{i} ==> {cities[i]}")
########################
# dic = { 'bill':'fill',"age":'33'}
# print(dic["age"])
# result =  "bill" in dic 
# print(result)
# print(list(dic.keys()))
# print(list(dic.values()))
# dic['billo'] = "viva"
# print(list(dic.items()))
################################
# numbers  = [ 1,2,4,3,2,1,7,5,8,5,3,5]
# sort = sorted(numbers)
# print(sort)
# numbers.remove(5)
# print(numbers)
# del(numbers[5])
# print(numbers)
# st = set(numbers) # remove duplicate and sort 
# print(st)
##############################################   classes 

# obj = {
#   'dim':"dim1",
#   'fill': "fil1"
# }
# print(obj["dim"])



# class  Planet:
#   def __init__(self):
#     self.name = "hill"
#     self.age = 77
#     self.height = 90
#     self.nationality = 'alg'

#   def oth(self):
#     return  print(self.name)

# bil = Planet()

# print(bil.name)
# print(bil.age)
# print(bil.height)
# print(bil.nationality)

# print(getattr(bil, 'name'))

# bil.oth()

###############################

class  Planet:

  active = True 
  def __init__(self, name, age, height, nationality):
    self.name = name
    self.age = age
    self.height = height
    self.nationality = nationality

  def oth(self):
    return  print(self.name)

  @classmethod
  def xi(cls):
    print(cls.active)
 

  @staticmethod
  def bio(age = 90):
    print(age)



  

newPlanet = Planet('hil', 33, 89, 'algerian')

print(newPlanet.name)
newPlanet.oth()

print(Planet.active)
Planet.xi()
newPlanet.xi()

Planet.bio(100)
newPlanet.bio(100)