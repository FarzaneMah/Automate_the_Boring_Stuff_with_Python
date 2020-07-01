import re
"""The ? says the group matches zero or one times.
The * says the group matches zero or more times.
The + says the group matches one or more times.
The curly braces can match a specific number of times.
The curly braces with two numbers matches a minimum and maximum number of times.
Leaving out the first or second number in the curly braces says there is no minimum or maximum.
"Greedy matching" matches the longest string possible, "nongreedy matching" (or "lazy matching")
 matches the shortest string possible.
Putting a question mark after the curly braces makes it do a nongreedy/lazy match."""




"""
\d any digit
\D any character that is not a numeric digit
\w any letter, numeric digit or underscore char
\W any char that is not any letter, numeric digit or underscore char
\s any space, tab, newline character
\S any character that is not a space, tab, newline
"""



batRegex = re.compile(r'Bat(wo)?man')#batRegex = re.compile(r'Batman|Batwoman')
match_object = batRegex.search('The adventures of Batman and Batwoman')
print(match_object.group())


batRegex = re.compile(r'Bat(wo)*man')#
match_object = batRegex.search('The adventures of Batwowowoman and Batwoman')
print(match_object.group())


batRegex = re.compile(r'Bat(wo)+man')#
match_object = batRegex.search('The adventure of Batman')
print(match_object)


haRegex = re.compile('(Ha){3}')
print(haRegex.search('HaHaHA'))
print(haRegex.search('HaHaHa'))


haRegex = re.compile('(Ha){3,5}')
print(haRegex.search('HaHaHA'))
print(haRegex.search('HaHaHaHaHaHAHA'))


#Greedy/Nongreedy
haRegex = re.compile('(\d){3,5}')
print(haRegex.search('12345678910'))
haRegex = re.compile('(\d){3,5}?')
print(haRegex.search('12345678910'))

from urllib.request import urlopen
from bs4 import BeautifulSoup
link = ""
file = urlopen('https://automatetheboringstuff.com/chapter7/')
html = file.read()#.decode('utf-8')
soup = BeautifulSoup(html)
#print(soup.prettify())
text = soup.get_text()
print(text)
#findall
haRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
print(haRegex.findall(text))

haRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
print(haRegex.findall(text))
