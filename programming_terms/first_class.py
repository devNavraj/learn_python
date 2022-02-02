'''
First-Class Functions: A programming language is said to have first-class
if it treats functions as first-class citizens.

First-Class Citizen (Programming): A first-class citizen (sometimes called)
first-class objects) in a programming language is an entity which supports
all the operations generally availale to other entities. These operations 
typically include being passed as an argument, returned from a function,
and assigned to a variable.
'''
# def square(x):
#   return x * x

# def cube(x):
#   return x * x * x

# f = square

# print(square)
# print(f(5))

# def my_map(func, arg_list):
#   result = []
#   for i in arg_list:
#     result.append(func(i))
#   return result

# squares = my_map(cube, [1, 2, 3, 4, 5])

# print(squares)

# def logger(msg):
#   def log_message():
#     print('Log:', msg)
#   return log_message

# log_hi = logger('Hi!')
# log_hi()

def html_tag(tag):
  def wrap_text(msg):
    print('<{0}>{1}</{0}>'.format(tag, msg))
  return wrap_text

print_h1 = html_tag('h1')
print_h1('Test Headline!')
print_h1('Another Headline!')

print_p = html_tag('p')
print_p('Test Paragraph!')