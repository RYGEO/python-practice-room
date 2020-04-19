"""In which we use classes and methods to display car information and
gradually modify a its odometer reading
Update 3 builds upon addition of child class "Electric Car"
and adds methods to analyze and update its battery size"""

class Car(object):
	"""represents car aspects"""
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.miles = 0

	def description(self):
		#Prints car's information
		print(self.year.title(), self.make.title(), self.model.title())

	def odometer(self):
		#Display car's mileage
		print("This car has travelled " + str(self.miles) + " miles.")

	def odometer_update(self, mileage):
		#Set mileage to new value - Method 2A
		if mileage >= self.miles:
			self.miles = mileage
		else:
			print("You can't roll back the odometer!")

	def odometer_increment(self, addmiles):
		#Set mileage to new value - Method 3A
		self.miles += addmiles

	def fill_gas_tank(self):
		print("This car's gas tank is now full.")

class ElectricCar(Car):
	"""represents electric car aspects"""
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery_size = 70

	def describe_battery(self):
		#prints a statement describing battery size
		print("This car has a " + str(self.battery_size) + "-kWh battry.")

	def fill_gas_tank(self):
		print("This car doesn't have a gas tank!")

	def get_range(self):
		#prints a statement about the range this battery provides
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
		message = "This car can go approximately " + str(range) + " miles on a full charge."
		print(message)

	def battery_update(self):
		self.battery_size = 85
		print("Car battery has been modified.")
		self.describe_battery()
			

"""Cars"""
car1 = Car("toyota", "camry", "2018")
car1.miles = 24000 #Set mileage to new value - Method 1
car2 = Car("ford", "fiesta", "2005")
car3 = ElectricCar("tesla", "model s", "2016")

"""car1.description()
car1.odometer()

car1.odometer_update(25000) #Set mileage to new value - Method 2B
car1.odometer()

car1.odometer_update(24500) #Testing if/else statement of odometer_update
car1.odometer()

car1.odometer_increment(100) #Set mileage to new value - Method 3B
car1.odometer()"""

car1.description()
car1.fill_gas_tank()
car3.description()
car3.describe_battery()
car3.fill_gas_tank()
car3.get_range()
car3.battery_update()
car3.get_range()
