import string

acronyms = {
    "lol": "laugh out loud",
    "dw": "don't worry",
    "hf": "have fun",
    "gg": "good game",
    "brb": "be right back",
    "g2g": "got to go",
    "wtf": "what the fuck",
    "wp": "well played",
    "gl": "good luck",
    "imo": "in my opinion"
}

print "Please enter the text to be expanded:"
text = raw_input()

for key, value in acronyms.items():
    text = string.replace(text, key, value)

print text
