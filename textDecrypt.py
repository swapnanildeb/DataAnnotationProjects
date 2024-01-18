def sortFunction(element):
	return int(element[0])

def decryptInput(inputArr):
	outputLines = []
	returnString = ""
	inputArr.sort(key=sortFunction)
	lineCounter = 1
	decodeCounter = 1
	decodeCounterIncrement = 2
	for x in inputArr:
		if lineCounter == decodeCounter:
			outputLines.append(x)
			decodeCounter += decodeCounterIncrement
			decodeCounterIncrement += 1
		lineCounter += 1
	for x in outputLines:
		returnString = returnString + x[1] + " "
	returnString.strip()
	return returnString

def main():
	input = open("coding_qual_input.txt", "r")
	inputLines = []
	for line in input:
		inputLines.append(line.split())
	result = decryptInput(inputLines)
	print(result)
	return result

if __name__=="__main__": 
    main() 



