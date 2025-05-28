class MyClass:
	def __init__(self,name,age):
		self.name=name
		self.age=age
		print('constructor called')
	def printer():
		print(f"Name:{self.name} Age:{self.age}")

obj = MyClass("manoj kumar",30)
#m.printer()
