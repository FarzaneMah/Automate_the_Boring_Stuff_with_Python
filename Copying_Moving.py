import shutil

Hello_File = open('hello2.txt', 'w')
Hello_File.write('Helllllooooooo!!!!!')
Hello_File.close()
shutil.copy('.\\hello2.txt','..\\')
#To rename
shutil.copy('.\\hello2.txt','.\\hello2_copy.txt')

#To copy a folder
#shutil.copytree('c:\\file','c:\\file_backup')

#move or/and rename
#shutil.move('c:\\file\\wall\\spam.txt', 'c:\\file\\wall\\spamspam_new.txt')
