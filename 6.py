import os
import shutil
file = input("Файл для удаления: ")
folder = input("Папка для удаления: ")
os.remove(file)
if input("Точно хочешь удалить эту директорию y/n: ") == "y":
    shutil.rmtree(folder)
else:
    print("Удаление отменено.")
