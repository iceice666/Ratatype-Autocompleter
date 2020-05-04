from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup

class API():
  def __init__(self) :
        #PATH
        self.PATH=os.path.dirname(__file__)
        self.sellang()
        self.chrome_options=webdriver.ChromeOptions()
        self.chrome_options.add_argument('--disable-gpu')
        self.chrome_options.add_argument('--hide-scrollbars')
        self.chrome_options.add_argument('blink-settings=imagesEnabled=false')
        self.run=webdriver.Chrome(executable_path=self.PATH+".\\assest\\chromedriver.exe",chrome_options=self.chrome_options)
        self.run.maximize_window()
        self.run.set_page_load_timeout(10)
        self.run.get("http://www.ratatype.com/login/")
        sleep(5)
        self.run.execute_script('window.stop()')
