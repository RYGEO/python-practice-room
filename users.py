"""This will what can be defined as user profile information.
There will be multiple users and the program will pull information
from various users as dictated by the program"""

class User():
	#user attributes
	def __init__(self, fname, lname, age, sex, loc, med, food):
		self.fname = fname #first name
		self.lname = lname #last name
		self.age = age #age in years
		self.sex = sex #sex of user (male/female/other/prefer not to say)
		self.loc = loc #location of user
		self.med = med #favorite work of media
		self.food = food #favorite food
	
	def login(self):
		print(self.fname.title(), self.lname.title() + " has logged in. How's it going,",\
			self.fname.title() + "?") #greets user that logs in

	def logout(self):
		print(self.fname.title() + " " + self.lname.title() + " has logged out.")
		#declares when user logs out

	def asl(self):
		print(self.fname.title() + " is", str(self.age) + "/" + self.sex.title() \
			+ "/" + self.loc.title() + ".")
		#provides age, sex, and location of user

	def interest(self):
		print(self.fname.title() + " is currently interested in " + self.med.title() + \
			"and eating " + str(self.food))
		#provides user's favorite work of media and food

#users
jack = User("jack", "jackson", "38", "male", "montreal, canada", "breaking bad",\
	"steak")
lori = User("lori", "laurens", "21", "female", "phoenix, arizona", "attack on titan",\
	"Twinkies")
eddie = User("eddie", "edwards", "47", "other", "edinburgh, ireland", "war and peace",\
	"apples")
hymn = User("hymnia", "methods", "29", "prefer not to say", "wouldn't you like to know " \
	";)", "a serbian film", "soylent green")

#methods
jack.login()
jack.asl()
jack.interest()
hymn.login()
hymn.asl()
hymn.interest()
eddie.login()
eddie.asl()
eddie.interest()
lori.login()
lori.asl()
lori.interest()
jack.logout()
lori.logout()
eddie.logout()
hymn.logout()