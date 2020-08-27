## Mellowdious
The main idea to find the flag is basing the 3 tones and decoding.

#### Step-1:
After we download `ctf.m4a`, when I listened it, I got a sense of 3 different cohesive tunes.

#### Step-2:
I got this script `base3.py` to execute:

```py
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
```
#### Step-3:
When it was executed as `python3 base3.py`, I got this output:

```bash
!-!'1
A�9?9NG

flag{3aRc4r3}
w u
±Ø¹³íB¹¤«DÛBî
ÄåÑÅë7ÑËÁ8â7ê
```

#### Step-4:
Finally, the flag becomes:
`flag{3aRc4r3}`