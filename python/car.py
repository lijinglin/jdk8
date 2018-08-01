class Car(object):
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.meter = 0
	
	def get_desc(self):
		long_name = str(self.year) + ' born ' + self.make + ' ' + self.model
		return long_name
	def read_meter(self):
		print "this car has " + str(self.meter) + ' miles on it'
	def inc_meter(self,miles):
		if miles < 0:
			print "you can not reduce miles"
			return;
		self.meter += miles;
class Battery:
	def __init__(self,battery_size = 70):
		self.battery_size = battery_size
	def get_size(self):
		return self.battery_size;
	def get_range(self):
		if self.battery_size == 70 :
			range = 240;
		elif self.battery_size == 85:
			range = 270
		return range
class ElectricCar(Car):
	def __init__(self,make,model,year,battery_size=70):
		#Car.__init__(self,make,model,year)
		super(ElectricCar,self).__init__(make,model,year)
		if(battery_size):
			self.battery = Battery(battery_size);
		else:
			self.battery = Battery();
	def get_desc(self):
		return Car.get_desc(self) + " the car can go " + str(self.battery.get_range()) + \
				" miles on a full charge"

tesla = ElectricCar('tesla','model s' ,2016)			
print tesla.get_desc()
	
	
tesla = ElectricCar('tesla','model s' ,2016,85)			
print tesla.get_desc()
		


	