import re
"""The regex method findall() is passed a string, and returns all matches in it, not just the first match.
If the regex has 0 or 1 group, findall() returns a list of strings.
If the regex has 2 or more groups, findall() returns a list of tuples of strings.
\d is a shorthand character class that matches digits. \w matches "word characters"
(letters, numbers, and the underscore). \s matches whitespace characters (space, tab, newline).
The uppercase shorthand character classes \D, \W, and \S match charaters that are not digits,
 word characters, and whitespace.
You can make your own character classes with square brackets: [aeiou]
A ^ caret makes it a negative character class, matching anything not in the brackets: [^aeiou]"""


lyrics = "12 drummers drumming, 11 pipers piping,\
 10 lords-a-leaping,\
 9 ladies dancing, 8 maids-a-milking,\
 7 swans-a-swimming, 6 geese-a-laying, 5 golden rings,\
 4 calling birds, 3 French hens, 2 turtle doves, and\
 a Le Creuset dutch oven because we love youuuuu."

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(lyrics))

print('-'*120)

vowelRegex = re.compile(r'[aeiouAEIOU]')#any vowel
print(vowelRegex.findall(lyrics))

print('-.'*60)

vowelRegex = re.compile(r'[aeiouAEIOU]{2}')#any 2vowels in a row
print(vowelRegex.findall(lyrics))

print('_-'*60)

constantsRegex = re.compile(r'[^aeiouAEIOU]')#not vowel
print(constantsRegex.findall(lyrics))
