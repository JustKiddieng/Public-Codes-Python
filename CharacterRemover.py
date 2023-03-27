import os
import shutil

print('\n\n')
print('--------- Multiple Filename Remover ---------')
print('# This program will remove specific name in many files on your directory you input.')
directory = input('Enter specific directory (ex. C:\\Users\Acer\Desktop): ')
character_to_remove = input('Enter parts of name to remove (ex. yt1s.com - ): ')

try:
    directory_files = os.listdir(directory)  # get the list of files from the valid directory

    # loop all files in the directory
    characterExist = False
    for file in directory_files:  # iterate each file
        if character_to_remove in file:  # if the character you want to remove is in the current file
            temporary_name = file  # store the name of current file to temporary
            temporary_name = temporary_name.replace(character_to_remove, '')  # remove the character that you want
            moveFromThisDirectoryWithFile = directory + '\\' + file  # combine the directory and the old name of file
            moveToThisDirectoryWithFile = directory + '\\' + temporary_name  # combine the directory and the new name of file
            shutil.move(moveFromThisDirectoryWithFile, moveToThisDirectoryWithFile)  # move the filename using the directory and old filename to directory and new file name
            characterExist = True  # set the variable to True because it has character you want to remove that exist on any file in the directory
        else:
            continue   # if the character you want to remove does not exist on the current file then just continue to iterate

    if not characterExist:  # if the there is no character you want to remove that exist on any file
        print('\nLooks like the name you enter is not exist on the directory you enter. Please try it again.')
    else:  # else
        print('\nAll file with that characters has removed successfully!')
except:
    print('\nError: Maybe the directory you type is not valid or specific.')
    print('\nExample: \"C:\\Users\ACER\Downloads\MP3 Files\" and not \"Downloads\" or \"Desktop\" or \"Documents\", etc   ')
    print('You can try again.')


print('\nEmail deliriousmansano13@gmail.com if there is an error or bug on the script.')
print('Suggest any automation on my youtube channel and let me check if I can do it.')
print('\nThank you for using this. I hope it helps.')
print('\nProgram ended...')
