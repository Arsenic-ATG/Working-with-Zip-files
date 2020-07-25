import os, zipfile

os.chdir('location of the directory where zip file exits')
example_zip = zipfile.ZipFile("example.zip")
example_zip.extractall()
example_zip.close()