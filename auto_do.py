from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import time
import json
import os.path
import os
import sys
import tkinter as tk
from tkinter import ttk
import re
import subprocess
from lang import *
from switch import switch

__version__="v.1.4"

class Autocompleter():
    def __init__(self) :
        #PATH
        self.PATH=os.path.dirname(__file__)
        self.sellang()
        self.chrome_options=webdriver.ChromeOptions()
        self.chrome_options.add_argument('--disable-gpu')
        self.chrome_options.add_argument('--hide-scrollbars')
        self.chrome_options.add_argument('blink-settings=imagesEnabled=false')
        fnull = open(os.devnull, 'w')
        return1 = subprocess.call('ping 35.168.176.193', shell = True, stdout = fnull, stderr = fnull)
        if return1:
            self.error(self.get_dict_value(self.lang_dict,["error","Network_exception"]))
        else:
            fnull.close()

    def get_dict_value(self,obj,pathlist):
        obj=dict(obj)
        for l in pathlist:
            obj=obj[l]
        return obj

    def start(self):
        self.msgbox()

    def date(self):
        i=0
        _date=""
        if i == 0 :
            i+=1
        elif i >= 1:
            return _date
        #date
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

        _date="{year}{mon}{day}-{hour}{min}-{sec}".format(year=year,mon=mon,day=day,hour=hour,min=_min,sec=sec)
        return _date

    def exit(self):
        try:
            self.run.quit()
            self._sellang.destroy()
            self._msgbox.destroy()
            self._close.destroy()
            self._tkerror.destroy()
        except:
            pass
        finally:
            sys.exit(0)

    def sellang(self):
        with open(file="{}\\assest\\lang\\list.json".format(self.PATH),mode="r",encoding="utf-8") as f:
            self.__langList__=dict(json.load(f))

        self._sellang=tk.Tk()
        self._sellang.title("Select Language")
        self._sellang.iconbitmap(self.PATH+"\\assest\\ico\\war.ico")
        frm=tk.Frame(self._sellang)
        frm.pack(side="right",padx=5)
        lab=tk.Frame(frm)
        btn=tk.Frame(frm)
        lab.pack()
        btn.pack()
        lab1=tk.Label(lab,text="Select Language",font=("微軟正黑體",12))
        lab1.pack()
        self.comlist=tk.StringVar()
        com1=ttk.Combobox(lab,textvariable=self.comlist)
        ll=[]
        for i in self.__langList__.keys():
            ll.append(self.__langList__[i])
        com1["values"]=ll
        com1.current(0)
        com1.pack()
        btn_Continue_execution=tk.Button(btn,text="Next",font=("微軟正黑體",12),command=self.next)
        btn_Close=tk.Button(btn,text="Close",font=("微軟正黑體",12),command=self.exit)
        btn_Continue_execution.pack(side="left",padx=5)
        btn_Close.pack(side="right")
        self._sellang.geometry()
        self._sellang.mainloop()

    def next(self):
        self._sellang.destroy()
        cl={}
        for i in self.__langList__.keys():
            cl[self.__langList__[i]]=i

        for case in switch(cl[self.comlist.get()]):
            if case("en_US"):
                self.lang_dict=en_US().__langDict__
                break
            if case("zh_TW"):
                self.lang_dict=zh_TW().__langDict__
                break
            if case("ja_JP"):
                self.lang_dict=ja_JP().__langDict__
                break
            if case():
                self.lang_dict=en_US().__langDict__

    def msgbox(self):
        #tk
        self._msgbox=tk.Tk()
        self._msgbox.title(self.get_dict_value(self.lang_dict,["GUI_msgbox","title"]))
        self._msgbox.resizable(False, False)
        self._msgbox.iconbitmap(self.PATH+"\\assest\\ico\\war.ico")
        frm=tk.Frame(self._msgbox)
        frm.pack(side="right",padx=5)
        lab=tk.Frame(frm)
        btn=tk.Frame(frm)
        img=tk.Frame(self._msgbox)
        img.pack(side="left",padx=5)
        image_=tk.PhotoImage(file=self.PATH+"\\assest\\png\\war.png")
        img1=tk.Label(img,image=image_)
        img1.pack()
        lab.pack()
        lab1=tk.Label(lab,text=self.get_dict_value(self.lang_dict,["GUI_msgbox","lab1"]),font=("微軟正黑體",12))
        lab2=tk.Label(lab,text=self.get_dict_value(self.lang_dict,["GUI_msgbox","lab2"]),font=("微軟正黑體",12))
        lab3=tk.Label(lab,text=self.get_dict_value(self.lang_dict,["GUI_msgbox","lab3"]),font=("微軟正黑體",12))
        lab1.pack()
        lab2.pack()
        lab3.pack()
        btn.pack()
        btn_Continue_execution=tk.Button(btn,text=self.get_dict_value(self.lang_dict,["GUI_msgbox","BTN_Continue_execution"]),font=("微軟正黑體",12),command=self.input_ep)
        btn_Close=tk.Button(btn,text=self.get_dict_value(self.lang_dict,["GUI_msgbox","BTN_Close"]),font=("微軟正黑體",12),command=self.exit)
        btn_Continue_execution.pack(side="left",padx=5)
        btn_Close.pack(side="right")
        self._msgbox.geometry()
        self._msgbox.mainloop()

    def input_ep(self):
        try:
            self._msgbox.destroy()
        except:
            pass
        self._start=tk.Tk()
        self._start.title(self.get_dict_value(self.lang_dict,["GUI_input_ep","title"]))
        self._start.resizable(False, False)
        self._start.iconbitmap(self.PATH+".\\assest\\ico\\start.ico")
        self.e_text=tk.StringVar()
        self.p_text=tk.StringVar()
        _input=tk.Frame(self._start)
        _input.pack()
        lab1=tk.Label(_input,text=self.get_dict_value(self.lang_dict,["GUI_input_ep","lab1"]),font=("微軟正黑體",12))
        lab2=tk.Label(_input,text=self.get_dict_value(self.lang_dict,["GUI_input_ep","lab2"]),font=("微軟正黑體",12))
        lab3=tk.Label(_input,text=self.get_dict_value(self.lang_dict,["GUI_input_ep","lab3"]),font=("微軟正黑體",12))
        e_entry=tk.Entry(_input,font=("微軟正黑體",12),state=tk.NORMAL,textvariable=self.e_text,width=20)
        p_entry=tk.Entry(_input,font=("微軟正黑體",12),state=tk.NORMAL,textvariable=self.p_text,width=20,show="\u25CF")
        self.e_text.set(self.get_dict_value(self.lang_dict,["GUI_input_ep","email_input_default"]))
        p_entry.bind("<Return>",self._data_login_e)
        lab1.grid(row=0,column=1)
        lab2.grid(row=1,column=0)
        lab3.grid(row=2,column=0)
        e_entry.grid(row=1,column=1,columnspan=2)
        p_entry.grid(row=2,column=1,columnspan=2)
        btn=tk.Frame(self._start)
        btn.pack()
        btn_Start=tk.Button(btn,text=self.get_dict_value(self.lang_dict,["GUI_input_ep","BTN_Start"]),font=("微軟正黑體",12),command=self._data_login)
        btn_Start.pack()
        self._start.geometry()
        self._start.mainloop()

    def restart(self):
        self._tkerror.destroy()
        self.input_ep()

    def close(self) :
        try:
            self.run.quit()
        except:
            pass
        self._close=tk.Tk()
        self._close.title(self.get_dict_value(self.lang_dict,["GUI_close","title"]))
        self._close.resizable(False, False)
        self._close.iconbitmap(self.PATH+".\\assest\\ico\\war.ico")
        frm=tk.Frame(self._close)
        frm.pack(side="right",padx=5)
        lab=tk.Frame(frm)
        btn=tk.Frame(frm)
        img=tk.Frame(self._close)
        img.pack(side="left",padx=5)
        image_=tk.PhotoImage(file=self.PATH+"\\assest\\png\\war.png")
        img1=tk.Label(img,image=image_)
        img1.pack()
        lab.pack()
        lab1=tk.Label(lab,text=self.get_dict_value(self.lang_dict,["GUI_close","lab1"]),font=("微軟正黑體",12))
        lab2=tk.Label(lab,text=self.get_dict_value(self.lang_dict,["GUI_close","lab2"]),font=("微軟正黑體",12))
        lab3=tk.Label(lab,text=self.get_dict_value(self.lang_dict,["GUI_close","lab3"]),font=("微軟正黑體",12))
        lab1.pack()
        lab2.pack()
        lab3.pack()
        btn.pack()
        btn_Continue_execution=tk.Button(btn,text=self.get_dict_value(self.lang_dict,["GUI_close","BTN_Continue_execution"]),font=("微軟正黑體",12),command=self.is_)
        btn_Close=tk.Button(btn,text=self.get_dict_value(self.lang_dict,["GUI_close","BTN_Close"]),font=("微軟正黑體",12),command=self.exit)
        btn_Continue_execution.pack(side="left",padx=5)
        btn_Close.pack(side="right")
        self._close.geometry()
        self._close.mainloop()

    def error(self,msg):
        try:
            self.run.quit()
        except:
            pass
        self._tkerror=tk.Tk()
        self._tkerror.title(self.get_dict_value(self.lang_dict,["GUI_error","title"]))
        self._tkerror.resizable(False, False)
        self._tkerror.iconbitmap(self.PATH+".\\assest\\ico\\start.ico")
        frm=tk.Frame(self._tkerror)
        img=tk.Frame(self._tkerror)
        img.pack(side="left",padx=5)
        frm.pack(side="right")
        _input=tk.Frame(frm)
        _input.pack()
        btn=tk.Frame(frm)
        image_=tk.PhotoImage(file=self.PATH+"\\assest\\png\\error.png")
        img1=tk.Label(img,image=image_)
        img1.pack()
        lab1=tk.Label(_input,text=self.get_dict_value(self.lang_dict,["GUI_error","lab1"]),font=("微軟正黑體",12))
        lab2=tk.Label(_input,text=self.get_dict_value(self.lang_dict,["GUI_error","lab2_1"])+"\"{}\"".format(msg)+self.get_dict_value(self.lang_dict,["GUI_error","lab2_2"]),font=("微軟正黑體",12))
        lab3=tk.Label(_input,text=self.get_dict_value(self.lang_dict,["GUI_error","lab3"]),font=("微軟正黑體",12))
        lab4=tk.Label(_input,text=self.get_dict_value(self.lang_dict,["GUI_error","lab4"]),font=("微軟正黑體",12))
        lab1.pack()
        lab2.pack()
        lab3.pack()
        lab4.pack()
        btn.pack()
        btn_restart=tk.Button(btn,text=self.get_dict_value(self.lang_dict,["GUI_error","BTN_Restart"]),font=("微軟正黑體",12),command=self.restart)
        btn_close=tk.Button(btn,text=self.get_dict_value(self.lang_dict,["GUI_error","BTN_Close"]),font=("微軟正黑體",12),command=self.exit)
        btn_restart.pack(side="left",padx=5)
        btn_close.pack(side="right")
        self._tkerror.geometry()
        self._tkerror.mainloop()

    def settings(self):
        pass
        self.set=tk.Tk()

    def _data_login_e(self,event):
        self._data_login()

    def _data_login(self):
        self._start.destroy()
        self.ac=self.e_text.get()
        self.pw=self.p_text.get()
        self.login(self.ac,self.pw)

    def entry_word(self,css_selector,word,wait_sec) :
        #輸入文字
        word=word
        entry_list=list(word)
        self.run.find_element_by_css_selector(css_selector).clear()
        for entry_key in entry_list :
            self.run.find_element_by_css_selector(css_selector).send_keys(entry_key)
            time.sleep(wait_sec)

    def entry_key(self,word,WPM):
        word_list=list(word)
        sec=60/(WPM*5)
        print(sec)
        for wl in word_list :
            AC(self.run).send_keys(wl).perform()
            time.sleep(sec)

    def login(self,email,password) :
        self.run=webdriver.Chrome(executable_path=self.PATH+".\\assest\\chromedriver.exe",chrome_options=self.chrome_options)
        self.run.maximize_window()
        self.run.set_page_load_timeout(10)
        url="http://www.ratatype.com/login/"
        self.run.get(url)
        time.sleep(15)
        self.run.execute_script('window.stop()')
        time.sleep(3)
        try:
            self.run.find_element_by_css_selector("#email")
        except NoSuchElementException :
            self.error(self.get_dict_value(self.lang_dict,["error","Network_delay_is_too_high"]))
            self.run.quit()
        self.entry_word("#email",email,0.05)
        time.sleep(0.5)
        self.entry_word("#password",password,0.05)
        time.sleep(0.5)
<<<<<<< HEAD
        try:
            self.run.find_element_by_css_selector("#fauth > div.form-group.btn-group-auth > button").click()
        except NoSuchElementException:
            self.error(self.get_dict_value(self.lang_dict,["error","Website_was_updated"]))
=======
        self.run.find_element_by_css_selector("#fauth > div.form-group.btn-group-auth > button").click()
>>>>>>> 4e0fcf74f1aff7304049b10eae1654cd60a66f14
        time.sleep(2)
        try:
            self.run.find_element_by_css_selector("body > div.center > div > div > div > div.rightSide > div > div:nth-child(3)")
        except:
            self.keystart()
        self.error(self.get_dict_value(self.lang_dict,["error","Password_is_incorrect"]))
        self.run.quit()

    def keystart(self) :
        time.sleep(2)

        self.run.find_element_by_css_selector("body > div.center > div > div.rightSide > div > div:nth-child(7) > div.nextExercise > form > button").click()

        time.sleep(3)
        self.run.find_element_by_css_selector("#ui-id-1 > button").click()
        time.sleep(2)
        html_doc=self.run.page_source
        soup = BeautifulSoup(html_doc, 'html.parser')


        w=(soup.find("div",{"id":"str_in"}).string)
        time.sleep(3)



<<<<<<< HEAD
        self.entry_key(w,105)
=======
        self.entry_key(w,100)
>>>>>>> 4e0fcf74f1aff7304049b10eae1654cd60a66f14
        time.sleep(2)
        self.run.save_screenshot(".\\assest\\finish image\\{}.png".format(self.date()))
        time.sleep(1)
        self.close()
        #os.exit_(1)

    def is_(self):
        self._close.destroy()
        self.login(self.ac,self.pw)








if __name__ == "__main__" :
    pl=Autocompleter()
    pl.start()





