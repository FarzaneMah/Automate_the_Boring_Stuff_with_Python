"""The sub() regex method will substitute matches with some other text.
Using \1, \2 and so will substitute group 1, 2, etc in the regex pattern.
Passing re.VERBOSE lets you add whitespace and comments to the regex string passed to re.compile().
If you want to pass multiple arguments (re.DOTALL , re.IGNORECASE, re.VERBOSE),
combine them with the | bitwise operator."""
import re

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bill'))
print()
print(namesRegex.sub('X', 'Agent Alice gave the secret documents to Agent Bill'))

print()

namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bill'))
print()
print(namesRegex.sub('Agent \1*****', 'Agent Alice gave the secret documents to Agent Bill'))
print()
print(namesRegex.sub(r'Agent \1****', 'Agent Alice gave the secret documents to Agent Bill'))


#VERBOSE
PhoneNumber = re.compile(r'''
((\d\d\d-|   #area AreaCode
\(\d\d\d\)) #-or- area code with parens and no dash
\d\d\d       #first 3 digits
-           #dash
\d\d\d\d)   # 4 digits
''', re.IGNORECASE|re.DOTALL|re.VERBOSE)

print(PhoneNumber.findall('I am going to leave please call me at 345-657-8767 or (123)456-7896'))
