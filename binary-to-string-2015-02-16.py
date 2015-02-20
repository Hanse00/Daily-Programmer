input = raw_input()

binary_values = []

index = 0

while len(input) > index:
    binary_values.append(input[index:index + 8])
    index += 8

result = ""

for value in binary_values:
    result += chr(int(value, 2))

print result
