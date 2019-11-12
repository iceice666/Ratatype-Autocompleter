import os
import json
class langdict():
    def __init__(self):
        self.PATH=os.path.dirname(__file__)
        try:
            with open(file=".\\lang\\list.json",mode="r",encoding="utf-8") as f:
                self.__langList__=json.load(f)
        except:
            with open(file=self.PATH+".\\lang\\list.json",mode="r",encoding="utf-8") as f:
                self.__langList__=json.load(f)

    class zh_TW():
        def __init__(self):
            try:
                with open(file=".\\lang\\zh_TW.json",mode="r",encoding="utf-8") as f:
                    self.__langDict__=json.load(f)
            except:
                with open(file=langdict().PATH+".\\lang\\zh_TW.json",mode="r",encoding="utf-8") as f:
                    self.__langDict__=json.load(f)

    class en_US():
        def __init__(self):
            try:
                with open(file=".\\lang\\en_US.json",mode="r",encoding="utf-8") as f:
                    self.__langDict__=json.load(f)
            except:
                with open(file=langdict().PATH+".\\lang\\en_US.json",mode="r",encoding="utf-8") as f:
                    self.__langDict__=json.load(f)
