import os
import wget
import requests
import getpass

path = fr"C:\Users\{getpass.getuser()}\Charonum\Charon Explorer"
for item in os.listdir(path):
    if "setup.py" == item:
        pass
    else:
        item = os.path.join(path, item)
        os.remove(item)

response = requests.get('https://raw.githubusercontent.com/Charonum/WE_Code/main/Files.txt')
responsecontent = response.text
for file in responsecontent.split("\n"):
    file = file.replace("b'", "")
    file = file.replace("'", "")
    file = file.replace(r"\n", "")
    if file == "":
        pass
    else:
        url = f'https://raw.githubusercontent.com/Charonum/WE_Code/main/code/{file}'
        wget.download(url)

os.system("Search_Engine.pyw")
quit()
