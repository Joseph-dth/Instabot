from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time


class g_email:
    def __init__(self, driver):
        self.driver = driver

    def g_email(self):
        print('running 10_email.py')
        
        self.driver.get('https://10minutemail.net/')
        email = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#fe_text')))
        #b_email = b(email.get_attribute('innerHTML'), 'html.parser')
        email = email.get_attribute('value')
        print(email)
        return(email)

    def e_response(self):
        time.sleep(10)
        
        response = get_response(self.driver)
        while len(response) >6:
            self.driver.refresh()
            response = get_response(self.driver)
        self.driver.close()
        return (response)
def get_response(driver):
        response = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#maillist > tbody > tr:nth-child(2) > td:nth-child(2) > a')))
        print(response.text)
        response = response.text.split(' ')
        print(response)
        return(response[0])

