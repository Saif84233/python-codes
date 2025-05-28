class MyClass:
	def __init__(self,name,age):
		self.name=name
		self.age=age
		self.salary=0
	def printer(self):
		print(f"Name:{self.name} Age:{self.age}")

m = MyClass("manoj kumar",80)
print(m.name)
print(m.age)
print(m.salary)

m2=MyClass('amir khan',60)

m2.printer()
m.age=85
m.printer()
