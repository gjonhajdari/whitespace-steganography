# whitespace-steganography
A university team project in Data Security. Uses tabs and spaces to embed hidden messages inside of text files.

To get started create an new snow object and use the built methods to embed and extract the message.
```python
# Import the class
from snow import snow

# Create the object
object = snow([fileName], [message])

# Embed the message
object.embedMessage()

# Extract the message
print(object.extractMessage())
```

*Note: the length of the embedded message cannot exceed the number of spaces inside of the source material (text file given)*

## How it works
1. Encode the message
	- Convert characters of string to ascii values
 	- Convert ascii values to their binary counterparts
	- Convert bits to whitespaces (1 = tab, 0 = space)
	- Store the characters in a list
2. Embed the message
	- Read and store the contents of the file
	- Iterate through lines and replace every space with a character from the encoded message list (if ther are no more characters leave the rest of the spaces)
	- Write modified content in an output file
3. Decode the message
	- Read and store the contents of a file
	- Select and store all the whitespace characters (not including newline character)
	- Divide the list into 8 digit (bit) long parts
	- Convert whitespaces to bits (1 = tab, 0 = space)
	- Convert the bytes to ascii values
	- Finally convert the ascii values back to characters

## Collaborators
- Gjon Hajdari
- Hekuran Kokolli
- Haki Hoti
- Gyltene Sfishta