from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time
import login
import getpages
import profile_edit
import upload_photo

'''
username = 'duckmaster123321'
password = 'duck123321'

username = 'Abdiel47807'
password = 'SCdQISia49xDlHi'

username = 'Alessia.Farrell405'
password = '8RaglZFpDsNkm4r'
'''

username = 'Noah_Greenholt804'
password = 'iUKzMQT4XOkVMsr'


driver = 0

def main():
    global driver
    print('running scripts...')

    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--headless')
    #chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--incognito")


    chrome_options.add_argument("--window-size=1980,1080")

    driver = webdriver.Chrome(chrome_options=chrome_options)
    #driver = webdriver.Chrome()
    l = login.Login(driver, username, password)
    l.signin()
    p = profile_edit.edit_profile(driver)
    p.edit_profile()
    u = upload_photo.upload_photo(username, password)
    u.upload_init()
'''
class auto_init:
    def __init__(self, driver, user):
        self.driver = driver
        self.user = user

    def auto_init(self):
        p = profile_edit.edit_profile(driver)
        p.edit_profile()
        u = upload_photo.upload_photo(username, password)
        u.upload_init()
'''



if __name__== '__main__':
    main()