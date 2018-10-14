from math import sqrt
class Vector(object):
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def __abs__(self):
		return sqrt(self.x**2 + self.y ** 2)
	def __add__(self,other):
		return Vector(self.x + other.x , self.y + other.y)
	def __sub__(self,other):
		return Vector(self.x - other.x , self.y - other.y)
	def __mul__(self,scalar):
		return Vector(self.x * scalar , self.y * scalar)
	def __bool__(self):
		print ('call bool vector')
		return bool(self.x or self.y)
	def __repr__(self):
		return 'Vector :x=%r ,y=%r' % (self.x,self.y)
		
vector = Vector(3,4)
print( abs(vector)	)	

print( bool(vector))
print( bool(Vector(0,0)))
print( vector)
