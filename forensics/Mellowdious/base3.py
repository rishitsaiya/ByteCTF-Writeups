# !/usr/bin/python3

a = "weqwe wweee wewqw weqww wwwqe wqqe wewqw weeew weqee wqqw wweqe wqqe wwwqq".split(" ")
keys = [
    {"w":"0","e":"1","q":"2"},
    {"w":"0","e":"2","q":"1"},
    {"w":"1","e":"0","q":"2"},
    {"w":"1","e":"2","q":"0"},
    {"w":"2","e":"0","q":"1"},
    {"w":"2","e":"1","q":"0"}
]
out = []
for key in keys:
    tempset = []
    for word in a:
        tempword = []
        for letter in word:
            tempword += [key[letter]]
        tempset += [tempword]
    out += [tempset]
answers = []
for variation in out:
    h = ""
    for word in variation:
        sum = 0
        for letter in range(len(word)):
            sum += int(word[letter]) * 3 **(len(word)-letter-1)
        h += chr(sum)
    print(h)
