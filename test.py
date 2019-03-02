def say_hello(name):
    """Says hello"""
    #  print("hello world")
    print("Hello, "+ name)

def add_numbers(x, y):
   return x+y

say_hello("Andy! :)") # should print "Hello, Andy! :)"
print("Addition result: " + str(add_numbers(12, 3))) ## should print "Addition result: 15"
print("Addition result: " + str(add_numbers(12, 6))) ## should print "Addition result: 18"
