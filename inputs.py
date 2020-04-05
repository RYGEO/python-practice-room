"""
This is going to be where you take a user's input
in order to complete a problem
and establish variables
This is probably the furthest I got when I took C Programming in 2012
Wish me luck, gamers
El Psy Congroo
"""

uta = 54
twee = 17
lunk = 31
king = "kangaroo"
scip = "SCP-682"

usr = input("Hello. What is your name, young one?"\
	" I'm assuming you're a young one. ")
print("Hajimemashite,", usr, ".\n"\
	"I hope you can help with some tasks today.\n")

nmr = int(input("Give me a number to divide by: "))
print("Okay, so we're going to use", nmr, "for the following problem.\n"\
	"Our problem is", uta, "subtracted by", lunk, "all divided by", nmr)

pud = (uta - lunk) / nmr

print("Our answer is", pud, "!\n")

hil = int(input("Now give me a number to multiply by: "))
print("Now we're going to use", hil, "for this next problem.\n"\
	"Our problem is", twee, "multiplied by", hil, "added to", pud)

him = twee * (hil + pud)

print("Our answer is", him, "!\n")

print("Alright, now I need you to identify a specific animal.\n"\
	"It is native to Austrailia and likes to jump a lot.\n")

ges = 3
for guess in range(ges):
	ana = input("Do you think you know what it is? ")
	if(ana == king):
		print("Yeah, that's right, it's a", king)
		break
	if(ana == scip):
		print("You absolute bufoon, you caused SCP-682 to breach containment!")
		break
	elif(ana != king and ana != scip):
		print("No, not", ana, "\n")
		if(guess == 1):
			print("You have", ges - (guess + 1), "try left...")
		else:
			print("You have", ges - (guess + 1), "tries left...")
	if(guess == 2):
		print("You're all out of guesses, the answer was", king)
