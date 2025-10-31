import os, time

c = input()
os.system(c)
open("shell.log", "a").write(time.ctime() + " " + c + "\n")
