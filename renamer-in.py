import os

files, url_global = [], os.path.abspath(os.curdir)
path_exe = os.path.abspath(__file__).replace('py', 'exe')

for (url, dirs, files) in os.walk(url_global):
    for file in files:
        path_from = "{}\\{}".format(url, file)
        path_to = "{}\\{}".format(url, file.lower().replace(" ", "-"))
        if path_from != path_exe:
            os.rename(path_from, path_to)

try:
    os.remove(path_exe)
except FileNotFoundError as error:
    print(error)
except PermissionError as error:
    print(error)