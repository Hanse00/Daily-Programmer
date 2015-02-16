import string

text = raw_input("ISBN to validate: ")

text = string.replace(text, "-", "")

checksum = 0

for i, char in enumerate(text):
    if char == "X":
        char = "10"

    checksum += int(char) * (10 - i)

valid = checksum % 11 == 0

print "This ISBN is:", valid
