from urllib.request import urlopen
from pathlib import Path
import urllib
import re
from bs4 import BeautifulSoup
import requests
# importing required modules
import PyPDF2
#Create a regex for phone numbers
phoneRegex = re.compile(r'''
(
((\d\d\d)|(\(\d\d\d\)))? #area code
(\s|-)      #first separator
\d\d\d     #first 3 digits
-          #separator
\d\d\d\d  #last 4 digits
(((ext(\.)?\s)|x)
 (\d{2,5}))?           #extension
 )
''', re.IGNORECASE|re.DOTALL|re.VERBOSE)

#TODO: Create a regex for email addresses
emailRegex = re.compile(r'''
#some .+_thing@somthing.somthing
[a-zA-Z0-9_.+]+ #name part
@               #@ symbol
[a-zA-Z0-9_.+]+ #domain part

''', re.VERBOSE)
#ToDO: Get the txt
filename = Path('examplePhoneEmailDirectory.pdf')
link = 'https://automatetheboringstuff.com/files/examplePhoneEmailDirectory.pdf'
r = requests.get(link, stream = True)
filename.write_bytes(r.content)

# creating a pdf file object
pdfFileObj = open('examplePhoneEmailDirectory.pdf', 'rb')
# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# printing number of pages in pdf file
#print(pdfReader)
# creating a page object
pageObj = pdfReader.getPage(5)
# extracting text from page
#print(pageObj.extractText().rstrip('\n'))
text_1_page = pageObj.extractText().rstrip('\n')
text = text_1_page.replace('\n','')
print(text)
extractedPhoen = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text_1_page)

allPhoneNumbers = []

for phoneNumber in extractedPhoen:
    allPhoneNumbers.append(phoneNumber[0])

results = '\n'.join(allPhoneNumbers) + '\n' +'\n'.join(extractedEmail)

print(results)
