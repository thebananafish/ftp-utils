import os
from os.path import join

directory = "/home/user/projects/TEST/"

badFile = {'!':'', ' ': '_'}

badDir = {'!': '', ' ': '_', '.': ''}

for root, dirs, files in os.walk(directory, topdown = False):

    # Rename files in directories
    for name in files:
        newname = name

        ext = name.split('.').pop()

        for k, v in badFile.items():
            newname = newname.replace(k, v)

        newname = ('%s.%s' % ((newname.replace(('.%s' % (ext)), '').replace('.', '_'), ext)))

        os.rename(join(root, name), join(root, newname))

    # Rename directories
    for d in dirs:
        newDir = d
        for k, v in badDir.items():
            newDir = newDir.replace(k, v)
        os.rename(join(root, d), join(root, newDir))