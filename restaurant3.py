"""This program will use classes to name three restaurants, state what type
of food they have, and state whether is it open or closed

Update:
This will also use classes to show and add the number of customers served today
either by pre-programmed values or user-provided values

Update 2:
Adds new child class Ice Cream Stand to simulate an ice cream establishment
and to display its most popular flavors
"""

class Restaurant():

	def __init__(self, name, cuisine):
		self.name = name
		self.cuisine = cuisine
		self.number_served = 0

	def describe(self):
		#prints restaurant info
		print("This restaurant is named " + self.name.title() + \
                      ". They serve " + str(self.cuisine) + " food.")

	def open(self):
		#declares that restaurant is open
		print(self.name.title() + " is currently open!")
		self.served_reset()
		self.served_today()

	def close(self):
		#declares that restaurant is closed
		print(self.name.title() + " is currently closed...")

	def served_today(self):
		#displays total amount of customers
		print(self.name.title() + " has served " + str(self.number_served) \
			+ " customers today!")

	def served_reset(self):
		#resets customers served to zero
		self.number_served = 0

	def set_number_served(self):
		#sets number of customers to fixed amount (5)
		self.number_served = 5
		self.served_today()

	def add_served(self, add_served):
		#sets number of customers to fixed amount as dictated by coder
		self.number_served += add_served
		self.served_today()

	def ask_served(self):
		#sets number of customers to amount provided by user
		self.number_served = input("How many customers has " + self.name.title() + \
			" served? ")
		self.served_today()

	def ask_add_served(self):
		#adds to number of customers based on amount provided by user
		ask_add_served = input("How many customers has " + self.name.title() + \
		" served since then? ")
		self.number_served = int(self.number_served) + int(ask_add_served)
		"""must convert string variables into integer variables before
		you can print as a string, otherwise the integer will not
		'concatenate' and bring up errors. F@<%ing Python"""
		self.served_today()
		"""FIXED ERROR: see line 60
		error: cannot concatenate int to str... why?
		error shows up if this method is used after ask_served
		does not show up if used by itself...."""

class IceCreamStand(Restaurant):
	#Child Class "Ice Cream Stand," a type of restaurant
	def __init__(self, name, cuisine):
		super().__init__(name, cuisine)
		self.flavors = "chocolate-vanilla swirl, peanut butter cup, and strawberry cheesecake."

	def top_menu(self):
		#displays most popular flavorts
		print("This ice cream stand's top flavors are " + self.flavors)
		

#Variables (Restaurants)
oliv = Restaurant("olive garden", "Italian")
taco = Restaurant("taco bell", "Tex-Mex")
kent = Restaurant("kentucky fried chicken", "mostly fried")
cone = IceCreamStand("cone zone", "cold 'n sweet")

"""
oliv.describe()
oliv.open()
print("\n2 hours later...")
oliv.set_number_served()
print("\n6 hours later...")
oliv.add_served(25)
oliv.close()
print("\nThe next day...")
oliv.open()
print("\nHalf a day later...")
oliv.ask_served()
print("\nA few hours later...")
oliv.ask_add_served()
oliv.close()
#Rinse and repeat for other variables. May expand for more practice later on.
"""

cone.describe()
cone.open()
cone.top_menu()
