#In which we use classes and methods to display car information and
#gradually modify a its odometer reading

class Car(object):
	"""docstring for Car"""
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.miles = 0

	def description(self):
		#Prints car's information
		print(self.make.title(), self.model.title(), self.year.title())

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


"""Cars"""
car1 = Car("toyota", "camry", "2018")
car1.miles = 24000 #Set mileage to new value - Method 1
car2 = Car("ford", "fiesta", "2005")

car1.description()
car1.odometer()

car1.odometer_update(25000) #Set mileage to new value - Method 2B
car1.odometer()

car1.odometer_update(24500) #Testing if/else statement of odometer_update
car1.odometer()

car1.odometer_increment(100) #Set mileage to new value - Method 3B
car1.odometer()