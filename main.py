from snow import Snow

message = "Hello world!"
longMessage = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

test = Snow("input.txt", message)

test.embed_message()
print("Extracted text: " + test.extract_message())