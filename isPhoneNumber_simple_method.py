import re


message = 'Call me at 445-263-5695 tomorrow or at 458-765-7655 the day after that'
PhoneNumber = re.findall("\d\d\d-\d\d\d-\d\d\d\d", message)
print(PhoneNumber)
for i in range(len(PhoneNumber)):
    print('phone number is :' + PhoneNumber[i])
