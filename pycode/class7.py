class Human:
	def __init__(self):
		pass
	def canwalk(self):
		print("Human can walk 10 km every day")
class Boy(Human):
		def __init__(self):
			self.gender="Male"
			self.walk=10
		def canwalk(self):
			super().canwalk()
			print(f"{self.gender} can walk {self.walk}km")
b= Boy()
b.canwalk()
