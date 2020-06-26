import os
#os.walk returns 3 values: foldernames, subfolders, filenames

for folderName, subfolders, filenames in os.walk('..\\SQL'):
    print('The folder is ' + folderName)
    print('The subfolders in ' + folderName + ' are' + str(subfolders))
    print('The filenames in ' + folderName + ' are' + str(filenames))
    print()
    for file in filenames:
        if file.endswith('.py'):
            print(file)

    for subfolder in subfolders:
        if 'fishhh' in subfolder:
            osrmdir(subfolder)
