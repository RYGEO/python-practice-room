#This is to test a list of names as an array

names = ["Roger", "Eric", "Tate", "Ned"]

rog = names[0]
eri = names[1]

print(rog)
print(eri + "\n")

eri = names[0 + 1]

print(eri + "\n")

for x in names:
	print(x)

print(names)
names.append("Alan")
print(names)
names.pop(0)
print(names)
names.remove("Alan")
print(names)
names.clear()
names = ["Larry", "Karl", "Frank"]
print(names)