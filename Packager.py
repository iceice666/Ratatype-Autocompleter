import os
import time
import shutil as su
from auto_do import __version__ as ver

__version__="0.1"

#PATH
PATH=os.path.dirname(__file__)
today = time.localtime()
year=today.tm_year
mon=today.tm_mon
day=today.tm_mday
hour=today.tm_hour
_min=today.tm_min
sec=today.tm_sec
if mon < 10 :
    mon="0{month}".format(month=str(mon))
if day < 10 :
    day="0{day}".format(day=str(day))
if hour < 10 :
    hour="0{hour}".format(hour=str(hour))
if _min < 10 :
    _min="0{_min}".format(_min=str(_min))
if sec < 10 :
    sec="0{sec}".format(sec=str(sec))
date="{mon}{day}.{hour}{min}.{sec}".format(mon=mon,day=day,hour=hour,min=_min,sec=sec)
pn="Ratatype_Autocompleter_{}".format(ver)
su.copytree(src="{}\\base data".format(PATH),dst="{}\\{}\\data".format(PATH,pn))
os.system("pyinstaller -F {path}\\auto_do.py -i {path}\\icon.ico -n Autocompleter --distpath {PN} --specpath {path}\\spec".format(path=PATH,PN=pn))
time.sleep(5)
su.rmtree(path=PATH+"\\__pycache__")
su.rmtree(path=PATH+"\\build\\Autocompleter")
su.rmtree(path=PATH+"\\build")
su.rmtree(path=PATH+"\\spec")
