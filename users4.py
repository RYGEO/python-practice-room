"""This will what can be defined as user profile information.
There will be multiple users and the program will pull information
from various users as dictated by the program

Version 2 adds methods to simulate log-in attempts by the use

Version 3 adds child class to user: admnin

Version 4 adds new class, privileges, which stores and grants admin privileges"""

class User():
	#user attributes
	def __init__(self, fname, lname, age, sex, loc, med, food):
		self.fname = fname #first name
		self.lname = lname #last name
		self.age = age #age in years
		self.sex = sex #sex of user
		self.loc = loc #location of user
		self.med = med #favorite work of media
		self.food = food #favorite food
		self.login_attempts = 0
	
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
			" and eating " + str(self.food))
		#provides user's favorite work of media and food

	def print_login_attempts(self):
		print(self.fname.title() + " has attempted to log-in " + str(self.login_attempts) + " times.")

	def increment_login_attempts(self):
		print("Login failed: invalid username/password.")
		self.login_attempts = int(self.login_attempts) + 1

	def reset_login_attempts(self):
		self.login_attempts = 0

class Admin(User):
	#user class: admin
	def __init__(self, fname, lname, age, sex, loc, med, food):
		super().__init__(fname, lname, age, sex, loc, med, food)
		self.privileges = Privileges()

class Privileges():
	#admin's privileges
	def __init__(self, privileges=[]):
		self.privileges = privileges

	def show_privileges(self):
		print("\nPrivileges:")
		if self.privileges:
			for privilege in self.privileges:
				print("- " + privilege)
		else:
			print("- This user has no privileges.")
		"""had to look at ehmatthes' guide for this;
		note to self: try to figure out the logic behind how this works"""

#users
jack = User("jack", "jackson", "38", "male", "montreal, canada", "breaking bad",\
	"steak")
lori = User("lori", "laurens", "21", "female", "phoenix, arizona", "attack on titan",\
	"Twinkies")
hiro = Admin("hiro", "tanaka", "32", "male", "nara, japan", "metal gear solid 2", "takoyaki")

"""methods
jack.login()
jack.asl()
jack.interest()
lori.login()
lori.asl()
lori.interest()
jack.logout()
lori.logout()
jack.print_login_attempts()
jack.increment_login_attempts()
jack.print_login_attempts()
jack.increment_login_attempts()
jack.increment_login_attempts()
jack.increment_login_attempts()
jack.print_login_attempts()
jack.reset_login_attempts()
jack.print_login_attempts()
hiro.login()
hiro.asl()
hiro.interest()
hiro.logout()
"""
hiro.login()
#hiro.privileges.show_privileges()
#print("\nAdding privileges...")
hiro_privileges = [
	'can reset passwords',
	'can change usernames',
	'can pin threads',
	'can moderate threads',
	'can suspend accounts',
    ]
hiro.privileges.privileges = hiro_privileges
hiro.privileges.show_privileges()