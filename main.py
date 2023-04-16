from snow import snow

message = "Hello world!"
longMessage = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

test = snow("input.txt", message)

test.embedMessage()
# print(test.extractMessage())