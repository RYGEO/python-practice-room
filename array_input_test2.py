"""this is to test another user-inputted array
and involved both string and integer variables"""

user = []

name = input("What is your name? ")

age = int(input("How old are you? "))

user.append(name)
user.append(age)

print("So your name is " + user[0] + " and you're " + str(user[1]) + " years old.")