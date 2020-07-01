"""The open() function will return a file object which has reading and writing –related methods.
Pass ‘r' (or nothing) to open() to open the file in read mode. Pass ‘w' for write mode.
 Pass ‘a' for append mode.
Opening a nonexistent filename in write or append mode will create that file.
Call read() or write() to read the contents of a file or write a string to a file.
Call readlines() to return a list of strings of the file's content.
Call close() when you are done with the file.
The shelve module can store Python values in a binary file.
The shelve.open() function returns a dictionary-like shelf value."""

Hello_File = open('hello.txt', 'w')
Hello_File.write('Helllllooooooo!!!!!')

Hello_File.write('Helllllooooooo!!!!!')

Hello_File.write('Helllllooooooo!!!!!\n')

Hello_File.write('Heyyyyyy!!!!!\n')

Hello_File.write('Do you hear me???????!!!!!\n')

Hello_File.close()

Hello_File = open('hello.txt')
print(Hello_File.readlines())

import os
print(os.getcwd())

Hello_File = open('hello.txt', 'a')

Hello_File.write('Helllllooooooo!!!!!\n')
Hello_File = open('hello.txt')
print(Hello_File.readlines())
Hello_File.close()

import shelve
shelfFile = shelve.open('Newfile')
shelfFile['cats'] = ['ssss', 'mmmm', 'nnnn']
shelfFile.close()


shelfFile = shelve.open('Newfile')
print(shelfFile['cats'])

shelfFile.close()
shelfFile = shelve.open('Newfile')
print(shelfFile.keys())
print(list(shelfFile.keys()))
