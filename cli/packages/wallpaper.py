from urllib import request
from bs4 import BeautifulSoup
from datetime import datetime as dt
import requests,os



res=requests.get('https://bingwallpaper.com/')
soup=BeautifulSoup(res.text,"lxml")
image=soup.find('a',{'class':'cursor_zoom'}).find('img')
link=image.get('src')
    return link
link=get_image()
file_name = dt.now().strftime("%Y-%m-%d")
user = os.getenv('USER')
path='/root/Pictures/BingWallpapers'
full_path=os.path.join(path,file_name)
if not os.path.exists(path):
    os.mkdir(path)
with open(full_path, 'wb') as f:
    f.write(request.urlopen(link).read())
return full_path
full_path=download()
os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri file:///"+full_path)
