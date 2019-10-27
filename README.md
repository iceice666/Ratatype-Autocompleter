# Ratatype-Autocompleter
可以自動執行Ratatype英語打字訓練的程式。

## 程式架構

### class Autocompleter()
* **\_\_init\_\_**
* **控制器**
  * _data_login_e(event)
  * _data_login()

* **使用者介面**
  * start()
  * restart()
  * close()
  * msgbox()
  * input_start()
  * error()

* **模組**
  * date()
  * exit()
  * login(email,password)
  * keystart()
  * entry_word(css_selector,word,wait_sec)
  * entry_key(word,WPM)

# 使用須知
## **模組相依性**
__此程式會用到下列模組和函式：__
* __time__
* selenium
  *  __webdriver__
    * common
      * exceptions
        * NoSuchElementException
      * by
        * __By__
      * action_chains
        * __ActionChains__
    * support
      * __expected_conditions__
      * wait
        * __WebDriverWait__
* bs4
  * __BeautifulSoup__
* __time__
* __json__
* __os.path__
* __os__
* __sys__
* __tkinter__
* __re__