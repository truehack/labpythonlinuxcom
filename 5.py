import os
import shutil

filefolder = input()
towhat = input()

os.makedirs(towhat)
os.rename(filefolder, os.path.join(towhat, filefolder))
shutil.move(filefolder, os.path.join(towhat, filefolder))
