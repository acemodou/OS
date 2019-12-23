import os
from datetime import datetime
import subprocess

# To learn what is in this directory
#print(dir(os))

# print("Current working directory is {}: ".format(os.getcwd()))
# os.chdir('C:/Users/mjaw/Desktop/Personal/gitBase/')
# print("After changing directory {}: ".format(os.getcwd()))


#os.chdir('C:/Users/mjaw/Desktop/')
#os.mkdir can make only a single directory in the top level
#os.mkdir("AJI")

#os.makedirs can make top level and sublevel so is more preferred.
#os.makedirs("House/budget")

#os.chdir('C:/Users/mjaw/Desktop/House')
#os.removedirs('House/budget')
#print(os.listdir())

#This tells you when a folder or file was created.
# mod_time = os.stat('Personal').st_mtime
# # print(datetime.fromtimestamp(mod_time))

# Traverse through directories in python

#os.chdir('C:/Users/mjaw/Desktop/')
#
# folder_path = 'C:/Users/mjaw/Desktop/Personal'
#
# for dirpath, dirname, filenames in os.walk(folder_path):
#     print("Current path:", dirpath)
#     print("Directories:", dirname)
#     print("Files :", filenames)
#     print()

# print(os.path.isdir('Personal'))
# print(os.path.isfile('Personal'))
# print(os.path.splitext('Personal/gitBase/OS/os_module.py'))

#To learn most of os.path

# print(dir(os.path))

#Shell=True Can be a security hazard if you are using untrusted inputs
#use it when you are running the arguments your self and make sure is not with user input
#Shell=True list more info than when set to false

# subprocess.run('dir', shell=True)

# p1 = subprocess.run('dir', capture_output=True)
#print(p1.stdout.decode())
#p1 = subprocess.run('dir', stdout=subprocess.PIPE, text=True)

# Instead of directing to pipe we can direct it to a file

# with open("output.txt", 'w') as f:
#     p1 = subprocess.run('dir', stdout=f, text=True)


#python doesn't throw a subprocess error. Let's list a directory that doesn't exist

# p1 = subprocess.run(['dir', 'output.txt'])
# print(p1.returncode) # will return 0 if no error found

# now list a file that doesn't exist

# p1 = subprocess.run(['dir', 'aji.txt'], capture_output=True, text=True)
# print(p1.returncode) # will return non zero if no error found
# print(p1.stderr)

#note this will only work in linux since cat and grep are unix commands
# p1 = subprocess.run(['cat', 'output.txt'], capture_output=True, text=True)
#
# p2 = subprocess.run(['grep', '-n', 'test'], capture_output=True, text=True, input=p1.stdout)
# print(p2.returncode)
