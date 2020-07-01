"""Files have a name and a path.
The root folder is the lowest folder.
In a file path, the folders and filename are separated by backslashes on Windows and
forward slashes on Linux and Mac.
Use the os.path.join() function to combine folders with the correct slash.
The current working directory is the oflder that any relative paths are relative to.
os.getcwd() will return the current working directory.
os.chdir() will change the current working directory.
Absolute paths begin with the root folder, relative paths do not.
The . folder represents "this folder", the .. folder represents "the parent folder".
os.path.abspath() returns an absolute path form of the path passed to it.
os.path.relpath() returns the relative path between two paths passed to it.
os.makedirs() can make folders.
os.path.getsize() returns a file's size.
os.listdir() returns a list of strings of filenames.
os.path.exists() returns True if the filename passed to it exists.
os.path.isfile() and os.path.isdir() return True if they were passed a filename or file path."""

import os
os.path.join('folder1','folder2', 'file.txt')
print(os.path.join('folder1','folder2', 'file.txt'))

#current working directory
print(os.getcwd())

#change the current working directory to c
print(os.chdir('c:\\'))

#current working directory
print(os.getcwd())

#change the current working directory to ....
print(os.chdir(os.path.join('Users','Farzaneh', 'Automate_the_Boring_Stuff_with_Python')))

#current working directory
print(os.getcwd())

print()

print(os.listdir())

print()

print(os.path.abspath('spam.png'))


totalSize = 0
for filename in os.listdir('c:\\Users\\Farzaneh\\Automate_the_Boring_Stuff_with_Python'):
    if not os.path.isfile(os.path.join('c:\\Users\\Farzaneh\\Automate_the_Boring_Stuff_with_Python', filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join('c:\\Users\\Farzaneh\\Automate_the_Boring_Stuff_with_Python', filename))

print(totalSize)
