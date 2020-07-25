import zipfile,os

os.chdir('/Users/ankursaini/Desktop')
exampleZip = zipfile.ZipFile("example.zip")
print(exampleZip.namelist())

spam_info = exampleZip.getInfo('spam.txt')
print(spam_info.file_size)
print(spam_info.compress_size)
exampleZip.close()