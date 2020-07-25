import zipfile,os

os.chdir('location of the zip file you want to read')
exampleZip = zipfile.ZipFile("name of the zip file you want to open")
print(exampleZip.namelist())

spam_info = exampleZip.getInfo('name of the subfile of the zip file you want informatino about the size')
print(spam_info.file_size)
print(spam_info.compress_size)
exampleZip.close()