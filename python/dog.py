class Dog(object):
	def __init__(self,name,age=1):
		self.name = name.title()
		self.age = age
	
	def sit(self):
		print(self.name + "is now sitting")
	
	def roll_over(self):
		print(self.name + "is now rolling over")
	
	def desc(self):
		print "A dog named " +self.name + " age is " + str(self.age)