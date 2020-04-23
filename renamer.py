import os

files, url = [], input()

for (url, dirs, files) in os.walk(url):
    for file in files:
        print(file)
        os.rename("{}\\{}".format(url, file), "{}\\{}".format(url, file.lower().replace(" ", "-")))