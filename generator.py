from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup as b
import random


from bs4 import BeautifulSoup as b
import time

class generator:
    def __init__(self, driver):
        self.driver = driver


    def generate(self):
        print('generating name')
        
        self.driver.get('http://tools.jb51.net/aideddesign/rnd_userinfo')
        #but = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="locale"]')))
        #but.click()
        time.sleep(10)
        s1 = Select(self.driver.find_element_by_id('locale'))
        s1.select_by_value("en")
        but = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="generateName"]')))
        but.click()
        username = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="inputName"]')))
        #username = b(username.get_attribute('innerHTML'), 'HTML.parser')
        print(username.text)
        account_name = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="inputUsername"]')))
        print(account_name.text)
        
        account_name = account_name.text + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
        password = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="inputPassword"]')))
        email = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="inputEmail"]')))
        email = str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + email.text 
        '''
        self.driver.get('https://10minutemail.net/')
        time.sleep(6)
        email = self.driver.find_element_by_id("fe_text")
        print(email)
        print(email.prettify())
        email = email.get_attribute("value")
        '''
        user = [email, username.text, account_name, password.text]

        return(user)        

    