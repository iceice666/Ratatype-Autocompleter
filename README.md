# Ratatype-Autocompleter
The software that can automatically perform Ratatype English typing training.

## Function Tree

### class Autocompleter()
* **\_\_init\_\_**
```py
def __init__(self) :
    self.PATH=os.path.dirname(__file__)
    self.chrome_options=webdriver.ChromeOptions()
    self.chrome_options.add_argument('--disable-gpu')
    self.chrome_options.add_argument('--hide-scrollbars')
    self.chrome_options.add_argument('blink-settings=imagesEnabled=false')
```
* **Controller**
  * data_login_e
  * data_login


* **View**
  * _start
  * _restart
  * _close
  * _msgbox
  * _input_start
  * _error

* **Model**
  * _date
  * **_exit**
  * login
  * keystart
  * entry_word
  * entry_key

