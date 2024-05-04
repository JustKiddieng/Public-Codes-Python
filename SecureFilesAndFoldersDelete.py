# python built-in imports
import os, shutil, random, string, time, re  # for moving directory, listing files, get current working direc

names = []
namesCount = 0
choices = string.ascii_letters + string.digits




''' ---------------------- RenameAllFolders() start ----------------------'''


def RenameAllFolders():
    folderList = os.walk(dir)

    allFolderNamesWithRoot = []
    oldFolderNames = []
    removedFolderNames = []

    for root, folders, files in folderList:
        allFolderNamesWithRoot.append(f'{root}{folders}')

    for folder in allFolderNamesWithRoot:
        pattern = re.compile(r'\[.*')
        modifiedFolder = re.sub(pattern, '', folder)
        oldFolderNames.append(modifiedFolder)

        #removing the foldername
        pattern = re.compile(r'.*\\')
        match = re.search(pattern, modifiedFolder)
        if match:
            noFolderName = match.group(0)
            removedFolderNames.append(noFolderName)

    foldersCount = len(removedFolderNames)
    newRandomFolderNames = []

    for count in range(foldersCount):
        randomNames = [random.choice(choices) for count in range(30)]
        if (''.join(randomNames) not in newRandomFolderNames):
            newRandomFolderNames.append(''.join(randomNames))

    print(f'Renaming the folders...\n')

    del newRandomFolderNames[0]
    del oldFolderNames[0]

    # reverse the list from the bottom of the hierarchy folder so that it can renam
    oldFolderNames = oldFolderNames[::-1]
    removedFolderNames = removedFolderNames[::-1]

    for index, oldFolderName in enumerate(oldFolderNames):
        print(f'Renaming: {oldFolderName} to this: {removedFolderNames[index]}{newRandomFolderNames[index]}')
        os.renames(oldFolderName, f'{removedFolderNames[index]}{newRandomFolderNames[index]}')
    print(f'Successfully renamed all the folders...\n')




''' ---------------------- RenameAllFolders() end ----------------------'''



''' ---------------------- DeleteAllFilesAndFolders() start ----------------------'''

def DeleteAllFilesAndFolders():
    global dir
    print()
    print('Deleting all the file/s and folder/s...')
    try:
        shutil.rmtree(dir)
    except:
        print('There was an error deleting all files and folders...')
        pass

''' ---------------------- DeleteAllFilesAndFolders() end ----------------------'''


''' ---------------------- RenameAllFiles() start ----------------------'''


# renaming all the files
def RenameAllFiles():
    currentNewNameIndex = 0
    global fileList
    fileList = os.walk(dir)

    print('Renaming the files..')
    for root, folder, files in fileList:
        for file in files:
            sourceFile = f'{root}\\{file}'
            destinationFile = f'{root}\\{names[currentNewNameIndex]}'
            print('Renaming the files..', end='\r')
            print(f'Renaming {sourceFile} to {destinationFile}')
            shutil.move(sourceFile, destinationFile)
            currentNewNameIndex += 1
    renamingFilesStop = time.perf_counter()
    print(f'Successfully renaming all the files...\n')

    # truncating or changing the byte size of the file
    newFileSize = 0  # new file size

    fileList = os.walk(dir)
    for root, folder, files in fileList:
        for file in files:
            filePath = f'{root}\\{file}'
            with open(filePath, 'rb+') as file:
                file.truncate(newFileSize)

    # option for renaming the folders
    while True:
        wantFoldersRenameInput = input('Do you want rename all folders to random string? y-YES, n-NO: ')
        if wantFoldersRenameInput == ('y' or 'n'):
            RenameAllFolders()
            break
        else:
            print(f'Please type only "y" or "n"\n')

    # option for deleting the files
    toBeDeleted = False

    while True:
        userInput = input('Do you want to delete all the file/s and folder/s? (y-YES, n-NO):  ')
        if userInput == 'y':
            toBeDeleted = True
            break
        elif userInput == 'n':
            print('No files has been deleted...')
            break
        else:
            print('Please type only "y" or "n"\n')

    if toBeDeleted:
        DeleteAllFilesAndFolders()

''' ---------------------- RenameAllFiles() end ----------------------'''





''' ---------------------- PROGRAM START ----------------------'''
print('\n\n#################################################################')
print('############### DELETE FILES AND FOLDERS SECURELY ###############')
print('###################### BY JUSTKIDDIENG ##########################')
print('#################################################################')

print(f'\n!!!!!!!!!!!!!! IMPORTANT NOTICE !!!!!!!!!!!!!!')
print(f'Please be careful to use this script because you cannot undo IT and your files and folders will be gone forever.')
print(f'\nFeatures:')
print(f'- Rename all files and folders from specific folder')
print(f'- Delete all files data from specific folder')
print(f'- Delete all files and folders from specific folder')
print(f'- Malicious people cannot recover your delete files')
print('\n\n')




dir = ""
while True:
    try:
        dir = input('Enter the directory you want to delete all the files: ')
        os.chdir(dir)
        break
    except:
        print('Incorrect file path, please input a valid path....\n')

fileList = os.walk(dir)

for root, folderName, files in fileList:
    for file in files:
        namesCount += 1

for count in range(namesCount):
    randomNames = [random.choice(choices) for count in range(30)]
    if (''.join(randomNames) not in names):
        names.append(''.join(randomNames))

if namesCount == 0:
    print('There is no files in that directory.')

    fileList = os.walk(dir)
    isHaveFolder = False

    for root, folders, file in fileList:
        if len(folders) > 0:
            isHaveFolder = True

    if isHaveFolder:
        print('But there are folders.')
        print(f'')
        wantRenameInput = ""
        while True:
            wantRenameInput = input('\nDo you want to rename all of this folders? y-YES, n-NO: ')
            try:
                if wantRenameInput == ('y' or 'n'):
                    break
            except:
                print('Please type only "y" or "n"')

        print(f'wantRenameInput: {wantRenameInput}')

else:
    fileList = os.walk(dir)

    print(f'\n\n==================== ALL FILES ====================')
    for root, folderName, file in fileList:
        if len(file) > 0:
            for currentFile in file:
                print(f'file: {currentFile}')


    while True:
        userInput = input(f'\nIs that all the files? y-YES (continue to rename to random string), n-NO (abort program): ')

        if userInput == 'y':
            RenameAllFiles()
            break
        elif userInput == 'n':
            print('\nProgram aborted...')
            print('Program exited...')
            break
        else:
            print('Please type only "y" or "n"')


print('\n')
print(f'Contact deliriousmansano13@gmail.com if problem occurred...')
print(f'Program exited...')

''' ---------------------- PROGRAM END ----------------------'''
