import zipfile,os

os.chdir('location of the folder in which the zip file exitsts')
exampleZip = zipfile.ZipFile("name of the zip file you want to open")
print(exampleZip.namelist())

spam_info = exampleZip.getInfo('name of the subfile of the zip file you want information about the size')
print(spam_info.file_size)
print(spam_info.compress_size)
exampleZip.close()