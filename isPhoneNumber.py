def isPhoneNumber(text):
    if len(text) !=12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

message = 'Call me at 445-263-5695 tomorrow or at 458-765-7655 the day after that'
#print(isPhoneNumber('458-765-7655'))
FoundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('phone number:' + chunk)
        FoundNumber = True
if not FoundNumber:
    print("Couldn't find any phone numbers.")
