#Two S'es make it sharp. And spicy.
"""Umm;
This is gonna be a test of variable types
and basic syntax for Python
"""

#Variables
bei = 3
cao = 2 + 1
sun = "cat"
zhuo = "cat"
yun = True
cat = "dog"

#Playing with The Variables of the Three Kingdoms

oda = bei + cao
print(oda)
print(oda, "is made from adding", bei, "and", cao, "\n")

guan = oda - 11
print(guan)
print(guan, "is made from subtracting 11 from", oda)

if(sun == zhuo):
	print("These'r cats! :3 :3 :3")

if(zhuo == cat):
	print("These'r cats! :3 :3 :3")
else:
	print("Wait, I thought cat meant cat, not dog!")

print("Is cat cat or not cat?")
if(cat == "cat"):
	yun = True
else:
	yun = False

if(yun == True):
	print("Cat is in fact cat.")
elif(yun == False):
	print("There is no cat. There is no cat. The cat is a dog indeed.")
