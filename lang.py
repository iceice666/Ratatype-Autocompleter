import os
import json
class en_US():
    def __init__(self):
        with open(file=os.path.dirname(__file__)+"\\assest\\lang\\en_US.json",mode="r",encoding="utf-8") as f:
            self.__langDict__=json.load(f)

class zh_TW():
    def __init__(self):
        with open(file=os.path.dirname(__file__)+"\\assest\\lang\\zh_TW.json",mode="r",encoding="utf-8") as f:
            self.__langDict__=json.load(f)

class ja_JP():
    def __init__(self):
        with open(file=os.path.dirname(__file__)+"\\assest\\lang\\ja_JP.json",mode="r",encoding="utf-8") as f:
            self.__langDict__=json.load(f)

