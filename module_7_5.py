import os
import time

print("Текущая директория: ", os.getcwd())
if os.path.exists("second"): # exists принимает True если этот путь существует если да то он его открывает
   os.chdir("second") #если дериктория "second" существет то мы ее меняем с помощью методе ченчь дир chdir
else:
    os.mkdir("second") # Создаем папку в этой директории
    os.chdir("second")
#print("Текущая директория: ", os.getcwd())
# os.makedirs(r"third\fourth")# создаем в папки секоннд еще две папки
# для того чтоб посмотреть файлы или фалы существует вот этот метод
#print(os.listdir())
#  Что бы проверить сколько папок  и файлов находятся в директорииия  нужно воспользоваться функцией которая приведена
#  ниже
# for f in os.walk("."):
#     print(f)

#os.chdir(r"C:\Users\user\PycharmProjects\Учеба\module_7_5\pythonProject1")
#print("Текущая директория: ", os.getcwd())

#file = [f for f in os.listdir() if os.path.isfile(f)]# отфильтровываем файлы
#dirs = [d for d in os.listdir() if os.path.isdir(d)]# отфильтровываем директории

#print(file)
#print(dirs)
# os.startfile(file[0])# запуск файла по индексу
#print(os.stat(file[1]))# получаем   информацию он файлке когда он был созда, открывался и т.д.
#print(os.stat(file[1]).st_size)# .st_size выводит размер файла в байтах
#os.system("pip install random2") # дает информацию о том установлен та или  иная библиотека
directory = r"C:\Users\user\PycharmProjects\Учеба\module_7_5\pythonProject1"
for root, dirs, files in os.walk(directory):
     for file in files:
         filepath = os.path.join(root, file)# полный путь к файлу root путь к файлу file- имя файла
         filetime = os.path.getmtime(filepath)
         formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime)) #Для модуля time нужно
         # импортировать import time чтоб все заработалл
         filesize = os.path.getsize(filepath) # узнаем размер файла
         parent_dir = os.path.dirname(file)
         print(
             f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time},'
             f' Родительская директория: {parent_dir}')
