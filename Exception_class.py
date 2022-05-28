class Usererror(RuntimeError):
   def __init__(self, arg):
      self.args = arg
try:
   raise Usererror("userError")
except Usererror as e:
   print (e.args)
