
from package.planet import Planet
from package.other import printed

printed()
hilal = Planet('hilal', 33, 'algerian', 'no')


hilal.console()
Planet.bill()
hilal.bill()
Planet.fill('green')
hilal.fill('green')


print('name ====> ', hilal.name)
print('age  ====> ', hilal.age)
print('nationality ====> ', hilal.nationality)
print('married  ====> ', hilal.married)
print('lang  ====> ', hilal.lang)
print('lang ====> ', Planet.lang)
