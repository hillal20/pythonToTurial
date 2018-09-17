from packages.calculation import calculate
from packages.classes import Project


newProject = Project('school', 30)
result = calculate(2,4)

print(newProject.name)
print(newProject.show())

print(result)
##########################################
words = [1,3,4,8.3,3,6]
def addTow(x):
   return x + 2
result = map(addTow, words)
print(list(result))
########################################

numbers = [1,2,3,4,5,7,9]
def greaterThen4(x):
    return x > 4
res =  filter(greaterThen4,numbers )
print(list(res))
###############################

num = [1,2,3,4,5,7]
lambda n: n * n 
r = map(lambda n:n*n, num)
print(list(r))