import pprint
from urllib.request import urlopen

link = "http://automatetheboringstuff.com/files/rj.txt"
file = urlopen(link)
text = file.read().decode('utf-8')
#text = "hasbdahsdagsd jashdkajsh"

count = {}
for char in text.upper():
    count.setdefault(char, 0)
    count[char] = count[char]+ 1

pprint.pprint(count)
#print(count)
