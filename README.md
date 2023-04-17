# whitespace-steganography
A university team project in Data Security. Uses tabs and spaces to embed hidden messages inside of text files.

To get started create an new snow object and use the built methods to embed and extract the message.
```python
# Import the class
from snow import snow

# Create the object
object = snow([fileName], [message])

# Embed the message (creates an output.txt file)
object.embedMessage()

# Extract the message
print(object.extractMessage())
```

*Note: the length of the embedded message cannot exceed the number of spaces inside the source material (text file)*

## How it works
1. Encode the message
	- Convert characters of string to ascii values
 	- Convert ascii values to their binary counterparts
	- Add padding if needed to make it an 8 bit value
	- Convert bits to whitespaces (1 = tab, 0 = space)
	- Store the characters in an array
2. Embed the message
	- Read and store the contents of the file
	- Iterate through lines and replace every space with a character from the encoded message array (if there are no more characters leave the rest of the spaces as they are)
	- Write modified content in an output file
3. Decode the message
	- Read and store the contents of a file
	- Select and store all the whitespace characters (not including newline character)
	- Divide the array into 8 digit (bit) long subarrays
	- Convert whitespaces to bits (1 = tab, 0 = space)
	- Convert the bytes to ascii values
	- Finally convert the ascii values back to characters

## Collaborators
- [Gjon Hajdari](https://github.com/GjonHajdari)
- [Hekuran Kokolli](https://github.com/hekurani)
- [Haki Hoti](https://github.com/HakiHoti)
- [Gyltene Sfishta](https://github.com/gyltenesfishta)