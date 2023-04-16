import time
from termcolor import colored

class snow:
	def __init__(this, fileName, message):
		this.fileName = fileName
		this.message = message

	def embedMessage(this):
		startTime = time.time()
		encodedMessage = encodeMessage(this.message)
		# Check if the message is longer than the available space
		if (len(encodedMessage) > this.countSpaces()):
			print(colored("The message is too long to embed in the text.", 'light_red'))
			return
			
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

		print(colored("Text hidden successfully!", 'light_green'))
		print("Time elapsed: %s seconds" % (time.time() - startTime))
        def decoder(self):
                array = []
                bits = ''
                array2 = []
                i = 0
                with open(self.fileName, "r") as file:
                content = file.read()
                spaces_list = re.findall(r'\s+', content)
                if len(spaces_list) % 8 != 0:
                    raise ValueError("Nuk eshte nje fjal komplete")
                else:
                    for char in spaces_list:
                         bits += convertToBits(char)
                         if len(bits) == 8:
                                 array2.append(bits)
                                 bits = ''
                    
                print(generate_word(array2));
	def extractMessage(this):
		return

	def countSpaces(this):
		with open(this.fileName, "r") as file:
			contents = file.read()
			# Count the amount of space characters
			whitespaces = contents.count(" ")
		return whitespaces
	
	
def encodeMessage(message):
	binaryArray = []
	encodedMessage = []

	for char in message:
		# Convert character to ascii, then binary and remove the 'Ob' prefix from the character
		binary_character = bin(ord(char))[2:]
		# Add to the array
		binaryArray.append(binary_character)
	# Convert the binary array to an array of whitepace characters
	for byte in binaryArray:
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
    if len(whitespace) == 3:
        return '1'
    else:
        return '0'
def generate_word(array):
    word = '';
    for value in array:
        decimal_num = int(value, 2)
        word += chr(decimal_num)
        print(decimal_num);
    return word;
