"""^ means the string must start with pattern, $ means the string must end with the pattern.
Both means the entire string must match the entire pattern.
The . dot is a wildcard; it matches any character except newlines.
Pass re.DOTALL as the second argument to re.compile() to make the . dot match newlines as well.
Pass re.I as the second argument to re.compile() to make the matching case-insensitive."""

import re

startHelloRegex = re.compile(r'^Hello') #If "Hello" is at the beginning
print(startHelloRegex.search('HelloThere I am here').group())
print(startHelloRegex.search('Oh HelloThere I am here'))

print()

endThereRegex = re.compile(r'There$') #If "Hello" is at the beginning
print(endThereRegex.search('HelloThere').group())
print(endThereRegex.search('Oh HelloThere I am here'))

print()


atRegex = re.compile(r'.at')#anything but not newline
print(atRegex.findall('The cat at the hat sat on the flat mat.'))

print()

atRegex = re.compile(r'.{1,2}at')#anything but not newline
print(atRegex.findall('The cat at the hat sat on the flat mat.'))

print()

text = 'First Name: Al Last Name: Swet'
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall(text))


print()
print('Greedy vs Nongreedy')
serve = '<To serve humans> for dinner.>'
nongreedy = re.compile(r'<(.*?)>')
print(nongreedy.findall(serve))
print()
greedy = re.compile(r'<(.*)>')
print(greedy.findall(serve))


prime = 'Serve the public trust.\nProtect the innocent.\nUpload the law.'
print(prime)

print()

dotStar = re.compile(r'.*')
print(dotStar.search(prime).group())
print()
print(dotStar.findall(prime))
print()
dotStar = re.compile(r'.*', re.DOTALL)
print(dotStar.search(prime).group())

print()

vowelRegex = re.compile(r'[aeiou]', re.IGNORECASE)
print(vowelRegex.findall('WOW! This is happening for ME!'))
