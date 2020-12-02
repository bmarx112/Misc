import os

#This code recursively builds a symmetric directory of folders specified by a user.
#The number of folders created on the lowest level is the product of the sum of folders on each subdirectory level
#The total number of folders is the sum of these products on every directory level

st = input("Enter Directory Path: ")

try:
    os.chdir(st)

except Exception as e:
    print(st,"is an invalid directory. Please enter proper directory path.")
    print("Error:",e)
    quit()

filepath = [st]

#error catching done above, so not needed for functions
def createFolder(ref):
    if not os.path.exists(ref):
        os.makedirs(ref)
    else:
        print("Path already exists.")
    return

def buildDirectory(path):
    sub = []
    print("-"*25)
    while True:
        #add names for folders
        name = input("Enter folder name: ")
        if name == "": break
        sub.append(name)

    ext_path = []
    if len(sub) == 0:
        for i in path:
            createFolder(i)
        return

    else:
        for n in path:
            for i in sub:
                ext_path.append(n+"\\"+i)
        return buildDirectory(ext_path)

print("\nBuild directory: \n\nWhen you have added all your folders for a sub-directory level, \nhit 'enter' without typing anything to move to the next layer. \nWhen you are completely finished, hit 'enter' without typing in any folders for a directory level.\n")
buildDirectory(filepath)
