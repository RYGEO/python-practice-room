"""this is to test 2 user-provided lists of digits:
One with a pre-defined number of digits to enter
The other with a user-defined number of digits to enter"""

num = []

x = int(3)

print("Enter 3 numbers:")

for y in range(0, x):
	inp = int(input())

	num.append(inp)

print(num)

num.clear()

z = int(input("Enter number of elements: "))

print("Now enter " + str(z) + " numbers:")

for y in range(0, z):
	inp = int(input())

	num.append(inp)

print(num)
