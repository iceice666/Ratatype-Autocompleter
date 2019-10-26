# Ratatype-Autocompleter
可以自動執行Ratatype英語打字訓練的程式。

## 程式架構

### class Autocompleter()
* **\_\_init\_\_**
* **控制器**
  * data_login_e(event)
  * data_login()

* **使用者介面**
  * start()
  * restart()
  * close()
  * msgbox()
  * input_start()
  * error()

* **模組**
  * _date()
  * _exit()
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



* bs4  BeautifulSoup
* time
* json
* os.path
* os
* sys
* tkinter
* re