
import os
import shutil
filelist = []

#path of the the folder you want to sort
src = (r'C:\Users\'UserName'\Downloads') 


extOnly = set()


for listfile in os.listdir(src):
    for i in list(listfile):
        if i == ".":
            filelist.append(listfile)


for s in filelist:
    name, ext = s.split('.')
    extOnly.add(ext)

for k in extOnly:
    try:
        os.makedirs(k + "_Files")

    except FileExistsError:
        continue

for file in filelist:
    extFinal = file.split('.')
    try:
        os.rename(file, extFinal[1] + "_Files/" + file)
    except (OSError, IndexError):
        continue
