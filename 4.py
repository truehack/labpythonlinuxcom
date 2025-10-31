import os
import shutil
oldfile = input()
newfolder = input()

if not os.access(oldfile, os.R_OK):
    print("Нет прав на чтение файла")
os.makedirs(newfolder)
shutil.move(oldfile,os.path.join(newfolder, oldfile))
