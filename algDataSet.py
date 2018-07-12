import random

f = open("C:/Users/Toft/Documents/Skule/algdat/teksDokument.txt" , "w")




alfabetet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n","o","p","q","r","s","t","u","v","w","x","y","z"]

for i in range (1000): #antal lister
	linge = ""
	linge += alfabetet[random.randint(0,len(alfabetet)-1)]
	
	linge += ":"

	for x in range(10): #tallene 0 til 10
		for y in range (random.randint(0,100)): #antal av det spsifikke tallet

			linge+=str(x)
			linge+= ","
	linge += "9"

	f.write(linge)
	f.write("\n")
	print(linge)


f.close()