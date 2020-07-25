import os, zipfile

os.chdir('location of the directory where zip file exits')
example_zip = zipfile.ZipFile("name of the zip file")
example_zip.extractall()
example_zip.close()