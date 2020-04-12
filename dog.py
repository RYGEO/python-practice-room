"""More or less copied verbatim from "Python Crash Course"
This is a test of classes and will simulate two dogs
doing what dogs do best"""

class Dog():
	"""A simple attempt to model a Dog"""


	def __init__(self, name, age):
		#Initialize name and age attributes
		self.name = name
		self.age = age

	def sit(self):
		#Simulate a dog sitting in response to a command
		print(self.name.title() + " is now sitting.")

	def roll_over(self):		
		#Simulate rolling over in response to a command
		print(self.name.title() + " rolled over!")

my_dog = Dog("hamburg", 3)
your_dog = Dog("alpha", 5)

print("My dog's name is " + my_dog.name.title() + ".")
print("Your dog's name is " + your_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
print("Your dog is " + str(your_dog.age) + " years old.")

my_dog.sit()
your_dog.roll_over()
my_dog.roll_over()
your_dog.sit()
my_dog.sit()