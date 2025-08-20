import zipfile

with zipfile.ZipFile('archive.zip', 'w') as zip:
    zip.write('file1.txt')
    zip.write('file2.txt)