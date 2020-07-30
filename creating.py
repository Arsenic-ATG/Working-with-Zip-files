import zipfile

# opening the project in write mode (just like file handling)
object = zipfile.ZipFile('new.zip','w')

# writing the files to be insterted inside the porject ( compression algortithm used here is DEFLATED)
object.write('example.txt',compress_type = zipfile.ZIP_DEFLATED)

# closing the object of zipfile
object.close()