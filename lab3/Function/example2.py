#Creating a Function

def my_function():
  print("Hello from a function")
 
#Calling a Function
def my_function():
  print("Hello from a function")
my_function()

#Arguments
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#Number of Arguments
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#Arbitrary Arguments, *args

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#Keyword Arguments

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#Positional-Only Arguments

def my_function(x, /):
  print(x)
my_function(3)

#Keyword-Only Arguments

def my_function(*, x):
  print(x)
my_function(x = 3)

#Combine Positional-Only and Keyword-Only

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

#Recursion

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)