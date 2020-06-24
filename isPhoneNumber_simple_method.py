import re


message = 'Call me 222 at 445-263-5695 tomorrow or at 458-765-7655 the day after that'
PhoneNumber = re.findall("\d\d\d-\d\d\d-\d\d\d\d", message)
AreaCode = re.findall("(\d\d\d)-\d\d\d-\d\d\d\d", message)

for i in range(len(PhoneNumber)):
    print('phone number is :' + PhoneNumber[i])

for i in range(len(AreaCode)):
    print('Area code is :' + AreaCode[i])


####Second method!
