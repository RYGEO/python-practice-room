"""
Mad Lib v1.0

This program will prompt the user for inputs and assign said
in puts for the purpose of creating a mad lib, or a story that has
elements that change depending on what's written in empty spaces.

The coder utilizes their current knowledge of variables, inputs, and
the print function to achieve this.
"""

usr = input("Hey there! My name is Sotenbori Slugger. What about you? ")
print("\nOh, so you're called", usr + "? Nice to meet you!\n\n"
	"The reason you're here right now is because I want to tell a story,"\
	" but I'll need your help with some of the details."\
	" When we're done, I'll show you the finished story, and you're going"\
	" to play a very big part in it! Have fun!\n")

spt = input("Okay, let's start with a sport: ")

ss1 = input("\nNow give me the name of a country: ")

fd1 = input("\nNext name a food dish for me: ")

nmb = input("\nType out a two-digit number: ")

ryt = input("\nAlright, now name a royal title (e.g king,"\
	" princess, duke, etc.): ")

fna = input("\nNow type down a full name: ")

ss2 = input("\nGive me another country: ")

fnb = input("\nAnd another full name: ")

ana = input("\nAnd now an animal: ")

aj1 = input("\nPut down an adjective: ")

vg1 = input("\nType in a verb ending in -ing: ")

job = input("\nNow write in a job title (e.g. janitor, pilot,"\
	" nurse, etc): ")

bkt = input("\nMake up a book title or use a real one: ")

vb1 = input("\nNext up is a verb: ")

vln = input("\nNow give me a real or made up villainous name: ")

pn1 = input("\nAnd now give me a plural noun: ")

anb = input("\nName another animal for me: ")

adv = input("\nGive me an adverb next: ")

fd2 = input("\nOkay, now type down the name of a fruit: ")

vb2 = input("\nGood, now another verb: ")

vb3 = input("\nGreat, and another verb: ")

lnm = input("\nGet me a last name too: ")

pn2 = input("\nName an animal, but make it a plural (e.g. ducks,"\
	" geese, ants, etc): ")

fd3 = input("\nOne last food item please: ")

twn = input("\nNext up, name me a town or city: ")

tme = input("\nPut in a unit of time, in plural form: ")

hwd = input("\nNow namedrop an actor or director: ")

aj2 = input("\nCool, good choice, now write an adjective: ")

aj3 = input("\nAnd one last adjective: ")

fsh = input("\nName a fashion brand for me: ")

clo = input("\nAnd an article of clothing: ")

vg2 = input("\nGood, write down another verb ending in -ing: ")

loc = input("\nName a location: ")

nou = input("\nGive me a noun: ")

vb4 = input("\nA verb: ")

pn3 = input("\nAnd finally a plural noun: ")

print("\n\nAwesome, thanks for the help,", usr + "!\n"\
	"Without further ado, here's the story:\n\n")

print("Last weekend, the 28th annual", spt, "international championship"\
	" was held in the capital city of", ss1 + ". While the city is known mostly for"\
	" their", fd1 + ", but competitors from over", nmb, "countries vied to"\
	" win the title of", ryt, "of", spt + ". There were many crowd favorites,"\
	" like", fna, "from", ss2, "and", fnb + ", also known as \"the", ana + ".\""\
	" None of us, however, back then would have known about what would"\
	" transpire during this competition, nor could we anticipate who would"\
	" grab the title of", ryt, "of", spt + ". Indeed, no one could have ever"\
	" imagined that", usr, "would sweep the entire competition!\n")

print("Their road to victory couldn't be described as any less than", aj1 + ", as"\
	" their first match ended with their opponent", vg1, "and getting"\
	" disqualified as a result. Their second match with", fna, \
	"involved a", job, "running onto the field and claiming they they were,"\
	" in fact,", fna, "and that the one in the championships was an imposter!"\
	" The story of", usr, "can be compared to", bkt + ", where the hero had to",\
	vb1, "during his final confrontation with", vln, "while enclosed in a ring"\
	" of", pn1 + ". In their final game,", usr, "employed a strategy known as \"",\
	anb, adv, "reaches for", fd2 + ",\" which caused their opponent to", vb2,\
	"and", vb3, "like a little girl! Referee", lnm + ", who presided over the"\
	" championship match between", usr, "and", fnb, "\"the", ana + ",\" had this"\
	" to say: \"", usr, "had this game won as easily as a pack of", pn2,\
	" could eat 100 pounds of", fd3 + "!\"\n")

print(usr, "hails from our very own", twn, "and has been practicing", spt, "for"\
	" just a few", tme + ". Becoming the", ryt, "of", spt, "has made them not just"\
	" the talk of the town, but of individuals in the film and fashion communities."\
	" Famous Hollywood personality", hwd, "has offered to adapt the experiences of",\
	 usr, "into a film, titled \"The", aj2, "and the", aj3 + ",\" and", fsh, "has"\
	 " reached out to", usr, "in regards to relasing their own line of", clo + "s."\
	 " We asked", usr, "about what they wanted to do next and they responded by", vg2,\
	 " and laughing. They said, \"I think I'm going to", loc, "with my", nou, "and",\
	  vb3, "with", pn3 + "!\"\n\n\n")

print("Thank you for helping and reading my story", usr + "! Have a nice day. Bye-bye!")
