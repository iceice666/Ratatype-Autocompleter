from time import sleep
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
import re
#            ----------------------  plng_in class START   ----------------------

__version__="v.1.1.3_64bit_no_headless"

class plng_in():

    def __init__(self) :
        #PATH
        self.PATH=os.path.dirname(__file__)
        print(self.PATH)
        self.chrome_options=webdriver.ChromeOptions()
        self.chrome_options.add_argument('--disable-gpu')
        self.chrome_options.add_argument('--hide-scrollbars')
        self.chrome_options.add_argument('blink-settings=imagesEnabled=false')
        #self.chrome_options.add_argument('--headless')
        self._msgbox()

    def _date(self):
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

        date="{year}{mon}{day}-{hour}{min}-{sec}".format(year=year,mon=mon,day=day,hour=hour,min=_min,sec=sec)
        return date

    def _exit(self):
        try:
            self.run.quit()
        except:
            pass
        finally:
            os._exit(1)

    def _msgbox(self):
        #tk
        self.msgbox=tk.Tk()
        self.msgbox.title("警告")
        try:
            self.msgbox.iconbitmap(".\\data\\ico\\war.ico")
        except:
            self.msgbox.iconbitmap(self.PATH+".\\data\\ico\\war.ico")
        frm=tk.Frame(self.msgbox)
        frm.pack(side="right",padx=5)
        lab=tk.Frame(frm)
        btn=tk.Frame(frm)
        img=tk.Frame(self.msgbox)
        img.pack(side="left",padx=5)
        try:
            image_=tk.PhotoImage(file=".\\data\\png\\war.png")
        except:
            image_=tk.PhotoImage(file=self.PATH+"\\data\\png\\war.png")
        img1=tk.Label(img,image=image_)
        img1.pack()
        lab.pack()
        lab1=tk.Label(lab,text="警告",font=("微軟正黑體",12))
        lab2=tk.Label(lab,text="此軟體僅用於測試",font=("微軟正黑體",12))
        lab3=tk.Label(lab,text="要繼續嗎？",font=("微軟正黑體",12))
        lab1.pack()
        lab2.pack()
        lab3.pack()
        btn.pack()
        btn1=tk.Button(btn,text="繼續執行",font=("微軟正黑體",12),command=self.input_start)
        btn2=tk.Button(btn,text="結束",font=("微軟正黑體",12),command=self._exit)
        btn1.pack(side="left",padx=5)
        btn2.pack(side="right")
        self.msgbox.geometry("%dx%d+%d+%d"%(220,115,((self.msgbox.winfo_screenwidth()/2)-(220/2)),((self.msgbox.winfo_screenheight()/2)-(115/2))))
        self.msgbox.mainloop()


    def input_start(self):
        try:
            self.msgbox.destroy()
        except:
            pass
        self.start=tk.Tk()
        self.start.title("帳號密碼輸入")
        try:
            self.start.iconbitmap(".\\data\\ico\\start.ico")
        except:
            self.start.iconbitmap(self.PATH+".\\data\\ico\\start.ico")
        self.e_text=tk.StringVar()
        self.p_text=tk.StringVar()
        self.e_text.set("@kmhjh.kh.edu.tw")
        _input=tk.Frame(self.start)
        _input.pack()
        lab1=tk.Label(_input,text="Ratatype帳號密碼輸入",font=("微軟正黑體",12))
        lab2=tk.Label(_input,text="帳號：",font=("微軟正黑體",12))
        lab3=tk.Label(_input,text="密碼：",font=("微軟正黑體",12))
        e_entry=tk.Entry(_input,font=("微軟正黑體",12),state=tk.NORMAL,textvariable=self.e_text,width=20)
        p_entry=tk.Entry(_input,font=("微軟正黑體",12),state=tk.NORMAL,textvariable=self.p_text,width=20,show="\u25CF")
        p_entry.bind("<Return>",self.data_login_e)
        lab1.grid(row=0,column=1)
        lab2.grid(row=1,column=0)
        lab3.grid(row=2,column=0)
        e_entry.grid(row=1,column=1,columnspan=2)
        p_entry.grid(row=2,column=1,columnspan=2)
        btn=tk.Frame(self.start)
        btn.pack()
        btn1=tk.Button(btn,text="開始",font=("微軟正黑體",12),command=self.data_login)
        btn1.pack()
        self.start.geometry("%dx%d+%d+%d"%(250,115,((self.start.winfo_screenwidth()/2)-(250/2)),((self.start.winfo_screenheight()/2)-(115/2))))
        self.msgbox.mainloop()

        def settings(self):
            pass
            self.set=tk.TK()



    def data_login_e(self,event):
        self.data_login()

    def data_login(self):
        self.start.destroy()
        self.login(self.e_text.get(),self.p_text.get())

    def error(self,msg):
        self.run.quit()
        self._tkerror=tk.Tk()
        self._tkerror.title("錯誤")
        try:
            self._tkerror.iconbitmap(".\\data\\ico\\error.ico")
        except:
            self._tkerror.iconbitmap(self.PATH+".\\data\\ico\\start.ico")
        frm=tk.Frame(self._tkerror)
        img=tk.Frame(self._tkerror)
        img.pack(side="left",padx=5)
        frm.pack(side="right")
        _input=tk.Frame(frm)
        _input.pack()
        btn=tk.Frame(frm)
        try:
            image_=tk.PhotoImage(file=".\\data\\png\\error.png")
        except:
            image_=tk.PhotoImage(file=self.PATH+"\\data\\png\\error.png")
        img1=tk.Label(img,image=image_)
        img1.pack()
        lab1=tk.Label(_input,text="我們非常抱歉",font=("微軟正黑體",12))
        lab2=tk.Label(_input,text="由於您的\"{}\"".format(msg),font=("微軟正黑體",12))
        lab3=tk.Label(_input,text="導致軟體無法正常進行",font=("微軟正黑體",12))
        lab4=tk.Label(_input,text="請問您是要...",font=("微軟正黑體",12))
        lab1.pack()
        lab2.pack()
        lab3.pack()
        lab4.pack()
        btn.pack()
        btn1=tk.Button(btn,text="重新啟動",font=("微軟正黑體",12),command=self.restart)
        btn2=tk.Button(btn,text="結束",font=("微軟正黑體",12),command=self._exit)
        btn1.pack(side="left",padx=5)
        btn2.pack(side="right")
        self._tkerror.geometry("%dx%d+%d+%d"%(250,150,((self._tkerror.winfo_screenwidth()/2)-(250/2)),((self._tkerror.winfo_screenheight()/2)-(150/2))))
        self._tkerror.mainloop()

    def restart(self):
        self._tkerror.destroy()
        self.input_start()

    def entry_word(self,css_selector,word,wait_sec) :
        #輸入文字
        word=word
        entry_list=list(word)
        self.run.find_element_by_css_selector(css_selector).clear()
        for entry_key in entry_list :
            self.run.find_element_by_css_selector(css_selector).send_keys(entry_key)
            sleep(wait_sec)

    def entry_key(self,word,WPM):
        word_list=list(word)
        sec=60/(WPM*5)
        print(sec)
        for wl in word_list :
            AC(self.run).send_keys(wl).perform()
            sleep(sec)




    def login(self,email,password) :
        try:
            self.run=webdriver.Chrome(executable_path=".\\data\\chromedriver.exe",chrome_options=self.chrome_options)
        except:
            self.run=webdriver.Chrome(executable_path=self.PATH+".\\data\\chromedriver.exe",chrome_options=self.chrome_options)

        self.run.maximize_window()
        #self.run.set_page_load_timeout(10)
        url="http://www.ratatype.com/login/"
        self.run.get(url)
        sleep(15)
        self.run.execute_script('window.stop()')
        sleep(3)
        try:
            self.run.find_element_by_css_selector("#email")
        except NoSuchElementException :
            self.error("網路異常")
            self.run.quit()
        self.entry_word("#email",email,0.05)
        sleep(0.5)
        self.entry_word("#password",password,0.05)
        sleep(0.5)
        self.run.find_element_by_css_selector("#fauth > div.form-group.clearfix > button").click()
        sleep(2)
        try:
            self.run.find_element_by_css_selector("body > div.center > div > div > div > div.rightSide > div > div:nth-child(3)")
        except:
            self.keystart()
        self.error("密碼不正確")
        self.run.quit()

    def keystart(self) :
        sleep(2)

        self.run.find_element_by_css_selector("body > div.center > div > div.rightSide > div > div:nth-child(7) > div.nextExercise > form > button").click()

        sleep(3)
        self.run.find_element_by_css_selector("#ui-id-1 > button").click()
        sleep(2)
        html_doc=self.run.page_source
        soup = BeautifulSoup(html_doc, 'html.parser')


        w=(soup.find("div",{"id":"str_in"}).string)
        sleep(3)



        self.entry_key(w,65)
        sleep(2)
        self.run.save_screenshot(".\\data\\finish image\\{}.png".format(self._date()))
        sleep(1)
        self.close()
        #os.exit_(1)





    def close(self) :
        try:
            self.run.quit()
        except:
            pass
        self._close=tk.Tk()
        self._close.title("完成")
        try:
            self._close.iconbitmap(".\\data\\ico\\war.ico")
        except:
            self._close.iconbitmap(self.PATH+".\\data\\ico\\war.ico")
        frm=tk.Frame(self._close)
        frm.pack(side="right",padx=5)
        lab=tk.Frame(frm)
        btn=tk.Frame(frm)
        img=tk.Frame(self._close)
        img.pack(side="left",padx=5)
        try:
            image_=tk.PhotoImage(file=".\\data\\png\\war.png")
        except:
            image_=tk.PhotoImage(file=self.PATH+"\\data\\png\\war.png")
        img1=tk.Label(img,image=image_)
        img1.pack()
        lab.pack()
        lab1=tk.Label(lab,text="完成",font=("微軟正黑體",12))
        lab2=tk.Label(lab,text="您已完成",font=("微軟正黑體",12))
        lab3=tk.Label(lab,text="要繼續嗎？",font=("微軟正黑體",12))
        lab1.pack()
        lab2.pack()
        lab3.pack()
        btn.pack()
        btn1=tk.Button(btn,text="繼續執行",font=("微軟正黑體",12),command=self.is_)
        btn2=tk.Button(btn,text="關閉",font=("微軟正黑體",12),command=self._exit)
        btn1.pack(side="left",padx=5)
        btn2.pack(side="right")
        self._close.geometry("%dx%d+%d+%d"%(220,115,((self._close.winfo_screenwidth()/2)-(220/2)),((self._close.winfo_screenheight()/2)-(115/2))))
        self._close.mainloop()






    def is_(self):
        self._close.destroy()
        self.input_start()







#            ---------------------- plng_in  class END   ----------------------



#            ----------------------   netholiday auto do subject work START   ----------------------

if __name__ == "__main__" :
    try :
        pl=plng_in()
    except BaseException as e :
        print(e)
        sleep(5)

    sleep(3)





