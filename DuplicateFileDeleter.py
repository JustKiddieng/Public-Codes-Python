# contact deliriousmansano13@gmail.com if you have concern or suggestions
# visit my youtube channel if you want to know how this works: https://www.youtube.com/watch?v=OOBiy-8g2tY

import os
import hashlib

header =\
'''
+----+==============================+----+
+----+|   DUPLICATE FILE DELETER   |+----+
+----+|     by JustKiddieng        |+----+
+----+==============================+----+
'''
description = 'This program will look for the duplicate files in a specific folder given by the user based on their ' \
              'contents. The duplicate files to be deleted is the file who has longer names and the based file that ' \
              'will not deleted has the smallest filename.'

help = \
'''
Help:
    Enter the full folder you want to look for duplicates, if it has duplicates then type y for deleting all the duplicates, type n for don't.
'''

important = \
'''
Important:
    Be aware of your backup files with the same content as the original
'''

print(header)
print('Description:',description)
print(help, important)
print()

fileDirectory = input("Enter the full directory you want to look for duplicate files: ")
dirFileList = os.listdir(fileDirectory)  # list all the files on that directory and put it ony variable dirFileList

hashSHA256 = hashlib.sha256()  # set the hashing algorithm to check for the duplicates 

os.chdir(fileDirectory)  # change the directory or go to the fileDirectory

hashCollection = []  # colleciton of hashes to look for how many duplicates are there
duplicateHash = []  # number of duplicate hashes

# get the smallest filename
smallestFilenames = []  # list of smallest file names to be based from when showing based and duplicate files
smallestSize = 100  # used to based on the condition of what is the smallest filename in a group of duplicate hashes
previousIndex = 0  # used to based when the index or group of hashes change, then it will add the smallest filenames on previous index
smallestFileName = ''  # variable for setting the smallest filename to be added on smallestFilenames list

for filename in dirFileList:  # iterate or loop based on the number of files in the directory
    try:  # using try and except because reading some files cause an error in the permission to read it
        with open(filename, 'r') as file:  # reading the file
            data = file.read()  # read the file and set the contents to the variable data
            binaryData = data.encode('utf-8')  # encode the contents into binary to be able to hash it
            hashedFile = hashlib.sha512(binaryData).hexdigest()  # hash the binaryData and set it to variable hashedFile
            hashCollection.append(hashedFile)  # add the hashFile to the hashCollection list
    except:
        continue  # continue if an error occured so that it will continue to the next file even an error occurred


# count the number of hashes and if there is more than 2 then add to duplicateHash list
for index in range(len(hashCollection)):  # iterate based on the number of elements in the hashCollection list
    hashCount = hashCollection.count(hashCollection[index])  # get the count of current hash of hashCollection from all the hashes of hashCollection
    currentHash = hashCollection[index]  # get the current hash and set it to currentHash variable
    if hashCount >= 2 and currentHash not in duplicateHash:  # if the count of hash is greater or equal to 2 and is not already in duplicateHash list, then add it
        duplicateHash.append(currentHash)  # add the current hash to duplicateHash list


# create list for each duplicate hash for appending all
for index in range(len(duplicateHash)):  # iterate using the length or number of elements in the duplicateHash list
    exec(f'dup{index} = []')  # using exec method to execute statement in a custom string


# add all the filename in each list of duplicate
for index in range(len(duplicateHash)):  # iterate using the length of duplicateHash list
    for index2 in range(len(hashCollection)):  # iterate using the length of hashCollection list
        if duplicateHash[index] == hashCollection[index2]:  # if the current duplicate hash is the same as the current collection hash
            exec(f'dup{index}.append(dirFileList[index2])')  # add to the current duplicate list the current filename in the directory


# getting the smallest filenames in each list of duplicate hash
for index in range(len(duplicateHash)):  # iterate using the length of duplicateHash
    for index2 in range(len(eval(f'dup{index}'))):  # iterate using the length of current dupx list
        if index != previousIndex:  # if the current index is changed
            smallestFilenames.append(smallestFileName)  # add the smallest file name to list of smallest filenames
            smallestSize = 100  # reset the size of smallest size for the group of duplicate hashes
            exec(f"dup{previousIndex}.remove('{smallestFileName}')")  # then remove the smallest filename
            previousIndex = index  # change the previous index to the current index
        if len(eval(f'dup{index}[{index2}]')) < smallestSize:  # check if the length of the current dupx list and current content of it is lesser than smallestSize
            smallestFileName = eval(f'dup{index}[{index2}]')  # set the smallestFileName var to the current index of current dupx list
            smallestSize = len(eval(f'dup{index}[{index2}]'))  # set the smallestSize to the length of current index of current dupx list
        if index == len(duplicateHash)-1 and index2 == len(eval(f"dup{index}"))-1:  # if the current index is last and the current content of index is last also
            smallestFilenames.append(smallestFileName)  # add the smallest filename to the list of smallestFilenames list
            exec(f"dup{index}.remove('{smallestFileName}')")  # then remove again the smallest from the list

print()

if len(duplicateHash) > 0:  # if there is duplicate hashes or files
    print('##################################################################')
    for index in range(len(duplicateHash)):  # iterate using the length of duplicateHash list
        print(f'Base filename: {smallestFilenames[index]}')  # print the base file which has the smallest filename
        print(f'Duplicates:')
        for index2 in range(len(eval(f"dup{0}"))):  # iterate using the number of elements of the current dupx list
            print('\t', eval(f'dup{index}[{index2}]'))  # print the filename of the current dupx list which has the larger filenames
        print('##################################################################')

    while True:  # iterate until the user enter the correct or valid input
        isDelete = input('\nDelete all duplicates? Type y-YES, n-NO: ')  # ask the user to input
        print()
        if isDelete == 'y':  # if the user type y
            for index in range(len(duplicateHash)):  # iterate using the length of duplicateHash list
                for index2 in range(len(eval(f"dup{0}"))):  # iterate using the length of the current dupx list
                    if os.remove(eval(f'dup{index}[{index2}]')) is None:  # if removing the current duplicate file return None
                        print(f"{eval(f'dup{index}[{index2}]')} was deleted successfully")  # print the deleted notice
            print('\nAll duplicate files has been deleted')  # print after the end of deleting all the duplicate files
            break  # break or exit the loop
        elif isDelete == 'n':  # i f the user type n
            print('\nNo files has been deleted')  # print the notice that there was no deleted file
            break  # break or exit the loop
        else:
            print('Please try again and input y for YES and n for NO')  # print to type the valid input
else:  # if there was no duplicate files in the directory enterd by the user
    print('\nThere is no duplicate files in this folder')  # print what is going on

print('Program ended...')  # print that the program is ended
