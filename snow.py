import re
import time
from termcolor import colored


class Snow:
    def __init__(self, file_name, message):
        self.file_name = file_name
        self.message = message

    def embed_message(self):
        start_time = time.time()
        encoded_message = encode_message(self.message)

        # Check if the message is longer than the available space
        if len(encoded_message) > self.count_spaces():
            print(colored("The message is too long to embed in the text.", 'light_red'))
            return

        # Read the contents of the file and store them
        with open(self.file_name, "r") as file:
            content = file.read()

        # Loop through the array and replace each space character with an array element
        j = 0
        for i in range(len(content)):
            if content[i] == " ":
                if j < len(encoded_message):
                    # Copy the content before and after the whitespace and add an element in the middle
                    content = content[:i] + encoded_message[j] + content[i + 1:]
                    j += 1
                else:
                    break

        # Write back the new contents to the file
        with open("output.txt", "w") as file:
            file.write(content)

        print(colored("Text hidden successfully!", 'light_green'))
        print("Time elapsed: %s seconds" % (time.time() - start_time))

    def extract_message(self):
        with open("output.txt", "r") as file:
            content = file.read()

        whitespace_array = re.findall(r"[ \t]", content)
        # Iterate through array and create an array with subarrays consisting of 8 elements
        grouped_array = [whitespace_array[n:n + 8] for n in range(0, len(whitespace_array), 8)]

        byte = ''
        byte_array = []
        # Convert every whitespace to it's corresponding bit
        for item in grouped_array:
            for i in range(len(item)):
                byte += to_bit(item[i])

            byte_array.append(byte)
            byte = ''

        # Go through the array and convert every binary string to an ascii character
        extracted_message = ''
        for byte in byte_array:
            extracted_message += chr(int(byte, 2))

        return extracted_message

    def count_spaces(self):
        with open(self.file_name, "r") as file:
            contents = file.read()
            # Count the amount of space characters
            whitespaces = contents.count(" ")
        return whitespaces


def encode_message(message):
    binary_array = []
    encoded_message = []

    for char in message:
        # Convert character to integer ascii value
        ascii_value = ord(char)
        # Convert integer to binary number, remove the 'Ob' prefix and fill with padding to make 8 bits
        binary_character = bin(ascii_value)[2:].zfill(8)
        # Add to the array
        binary_array.append(binary_character)
    # Convert the binary array to an array of whitespace characters
    for byte in binary_array:
        for bit in byte:
            encoded_message.append(to_white_space(bit))

    return encoded_message


def to_white_space(bit):
    # Spaces represent a 0 and tabs represent a 1
    if bit == '1':
        return '\t'
    else:
        return ' '


def to_bit(whitespace):
    # Spaces represent a 0 and tabs represent a 1
    if whitespace == '\t':
        return '1'
    else:
        return '0'
