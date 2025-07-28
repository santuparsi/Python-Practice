x = -1
# To throw (or raise) an exception, use the raise keyword.
if x < 0:
  raise Exception("Sorry, no numbers below zero")

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")