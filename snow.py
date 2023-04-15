# 1. Encode message
#	1.1. Convert characters of string to ascii values
# 	1.2. Convert ascii values to binary
#	1.3. Convert bits to whitespace (1 = tab, 0 = space)
#	1.4. Store characters in a list
# 2. Embed the message
#	2.1. Read and store the contents of the file
#	2.2. Iterate through lines and replace every space with a character from the encoded message list
#	3.3. Write modified content in an output file
# 3. Decode the message
#	3.1. Read and store the contents of a file
#	3.2. Select and store all the whitespace characters (not including newline character)
#	3.3. Divide the list into 8 digit long parts
#	3.4. Convert whitespaces to bits (1 = tab, 0 = space)
#	3.5. Convert the bytes to ascii values
#	3.6. Finally convert the ascii back to characters

class snow:
	def __init__(this, fileName, message):
		this.fileName = fileName
		this.message = message

	def embedMessage(this):
		encodedMessage = encodeMessage(this.message)
		
		# Read the contents of the file and store them
		with open(this.fileName, "r") as file:
			content = file.read()
	
		# Loop through the array and replace each space character with an array element
		j = 0
		for i in range(len(content)):
			if (content[i] == " "):
				if (j < len(encodedMessage)):
					# Copy the content before and after the whitespace and add an element in the middle 
					content = content[:i] + encodedMessage[j] + content[i+1:]
					j += 1
				else:
					break
				
		# Write back the new contents to the file
		with open("output.txt", "w") as file:
			file.write(content)	
	
		print("Text embedded successfully!")

	def extractMessage(this):
		return
	
	def extractMessage(this):
		return
	
def encodeMessage(message):
	tempArray = []
	encodedMessage = []

	for char in message:
		# Convert character to ascii, then binary and remove the 'Ob' prefix from the character
		binary_character = bin(ord(char))[2:]
		# Add to the array
		tempArray.append(binary_character)
	# Convert the binary array to an array of whitepace characters
	for byte in tempArray:
		for bit in byte:
			encodedMessage.append(convertToWhitespace(bit))
	return encodedMessage

def convertToWhitespace(bit):
	# Spaces represent a 0 and tabs represent a 1
	if (bit == '0'):
		return ' '
	else:
		return '\t'
	
def convertToBits(whitespace):
	# Spaces represent a 0 and tabs represent a 1
	if (whitespace == '\t'):
		return '1'
	else:
		return '0'