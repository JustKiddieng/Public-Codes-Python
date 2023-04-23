# you need to install pymsgbox as external module/package - type "pip install pymsgbox" in command prompt if you are using windows os and os and shutil package/module are built-in in python
# pymsgbox is external package

# visit this link: https://www.youtube.com/watch?v=41j63ajBmPI if you want to know how this works.

# note that there
import os, shutil,pymsgbox as msg

def manageFile(targetPath):
    print(targetPath)
    os.chdir(targetPath)  #change the directory with absolute path
    allFileExtensions = []  #set a list variable

    #variable that will base on loop if the directory has a file with no extension
    hasFileWithNoExtension = False

    for i in range(len(os.listdir(targetPath))):  #set i to the numbers of all files and directories of the path
        if os.path.isfile((os.listdir(targetPath))[i]):  #check if current file is a file or directory
            fileName = os.listdir(targetPath)[i]  #put the current filename to a variable
            if '.' in fileName:
                rev_fileName = fileName[::-1]  #reverse the filename
                currentFileExtension = rev_fileName[:rev_fileName.index('.')][::-1]  #slice the reverse filename that start from beginning until before .
                if currentFileExtension not in allFileExtensions:  #check if the file extension name is not in allFileExtensions variable
                    allFileExtensions.append(currentFileExtension)  #if yes then append or add it to the variable
            else:
                hasFileWithNoExtension = True
    #creating folder for specific extensions that is found based on the file on the directory
    for x in range(len(allFileExtensions)):  #loop based on the number of allFileExtensions variable
        if (allFileExtensions[x].upper() + ' Files') not in os.listdir(targetPath):  #check if the folder exist on the current directory
            os.mkdir(allFileExtensions[x].upper() + ' Files')  #make folder if not
            print('Successfully created \'' + currentFileExtension.upper() + ' Files\' Folder!')
        else:
            print('Folder \'' + allFileExtensions[x].upper() + ' Files\' exist!')  #print the folder exist

    #create folder for no file extension name
    if hasFileWithNoExtension:
        if not os.path.exists('No extension name'):
            os.mkdir('No extension name')


    #moving files to their respective folders
    currentIndex = 0
    while True:
        hasFileExtension = True
        currentDirListCount = len(os.listdir(targetPath))

        if currentIndex == currentDirListCount:
            hasFileExtension = False

        if currentIndex < currentDirListCount:
            print('current index: ' + str(currentIndex))
            print('current dirlistcount: ' + str(currentDirListCount))
            print((os.listdir(targetPath))[currentIndex])
            if os.path.isfile((os.listdir(targetPath))[currentIndex]):  # check if current file is a file or directory
                fileName = os.listdir(targetPath)[currentIndex]  # put the current filename to a variable
                currentFileFullPath = os.path.join(targetPath, fileName)  # combine the current directory and the filename

                if '.' in fileName:
                    rev_fileName = fileName[::-1]  # reverse the filename
                    currentFileExtension = rev_fileName[:rev_fileName.index('.')][::-1]  # slice the reverse filename that start from beginning until before .
                    destinationFolder = os.path.join(targetPath, currentFileExtension.upper() + ' Files')  # set the destination of each folder

                    #check if the file name exists in the folder
                    if fileName in os.listdir(destinationFolder):
                        print(f'filename {fileName} exists in the destination folder')
                        currentIndex += 1 # continue to iterate the files
                    else: # if the filename is not exists in the destination folder then move it
                        shutil.move(currentFileFullPath, destinationFolder)  # move the files to their own folder extension name
                        currentIndex = 0  #go back to the first file
                else:
                    destinationFolder = os.path.join(targetPath, 'No extension name')  # set the destination of each folder
                    shutil.move(currentFileFullPath, destinationFolder)  # move the files to their own folder extension name
            else:
                currentIndex += 1  #if current file is directory then go to next
        else:
            break

while True:
    targetPath = msg.prompt('Enter the absolute path of the target folder (like C:\\Users\\User\\Downloads) or type \"this\" if you want this folder where this file belongs.', title='Manage File by JustKiddieng')
    print(f'target path: {targetPath}')

    try:
        if '\\' in targetPath and len(targetPath) > 1:
            #targetPath = targetPath[:targetPath.index('\\')] + '\\' + targetPath[targetPath.index('\\'):]
            if not (os.path.exists(targetPath)):
                msg.alert('The path you type does not exist!', title='Notice')
            else:
                manageFile(targetPath)
                msg.alert('The files successfully managed! Refresh the folder if nothing happened', title='Notice')
                msg.alert('Message the developer on deliriousmansano13@gmail.com if any error has occurred. Thanks', title='Notice')
                break
    except TypeError:
        break

    if targetPath == 'this':
        targetPath = os.getcwd()
        manageFile(targetPath)
        msg.alert('The files successfully managed! Refresh the folder if nothing happened', title='Notice')
        #msg.alert('Message the developer on deliriousmansano13@gmail.com if any error has occurred. Thanks.', title='Notice')
        break
    elif targetPath == 'x':
        msg.alert('This')
        exit()
    else:
        msg.alert('Please type the requirements or type \"x\" to exit the program or close the application.')
