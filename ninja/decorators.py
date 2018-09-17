


def helloDecorator(fn):
  def wrapper():
    print('ahahahahah')
    fn()
    print('hooooooo')
  return wrapper
  




@helloDecorator
def question():
  print('hello hillal')

question()

@helloDecorator
def foo():
  print('fooooo')
  
foo()