numOfCases = int(input())
for i in range(numOfCases):
	caseSize = int(input())
	DNA = input()
	
	if("U" in DNA):
		print("Error RNA nucleobases found!")
	else:
		DNAPair = ""
		for j in range(caseSize):
			if("A" in DNA[j]):
				DNAPair += "T"
			elif("T" in DNA[j]):
				DNAPair += "A"
			elif("C" in DNA[j]):
				DNAPair += "G"
			elif("G" in DNA[j]):
				DNAPair += "C"
		print(DNAPair)
