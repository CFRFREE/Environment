from os import environ
from os import getcwd
from os import listdir
from shutil import copy

name = environ['USERNAME']
FileFrom = getcwd() + "\\lib"
FileTo = "C:\\Users\\" + name + "\\AppData\\Roaming\\Sublime Text\\Packages\\user\\"

FileList = listdir(FileFrom)
for FileName in FileList:
	Name = FileFrom + "\\" + FileName
	# print(OldName)
	# print(NewName)
	copy(Name, FileTo)
