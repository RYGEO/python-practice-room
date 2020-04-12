"""This program will use classes to name three restaurants, state what type
of food they have, and state whether is it open or closed"""

class Restaurant():

	def __init__(self, name, cuisine):
		self.name = name
		self.cuisine = cuisine

	def describe(self):
		print("This restaurant is named " + self.name.title() + \
                      ". They serve " + str(self.cuisine) + " food.")

	def open(self):
		print(self.name.title() + " is currently open! :D")

	def close(self):
		print(self.name.title() + " is currently closed... :(")

oliv = Restaurant("olive garden", "Italian")
taco = Restaurant("taco bell", "\"Mexican\"")
kent = Restaurant("kentucky fried chicken", "Kentuckynese")

oliv.describe()
oliv.open()
taco.describe()
taco.open()
kent.describe()
kent.close()
