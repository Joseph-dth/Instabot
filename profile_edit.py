from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time
import pyautogui
import random


'''
element_present = EC.presence_of_element_located((By.XPATH, "//button[@title='Open file selector']"))  # Example xpath

WebDriverWait(self.driver, 10).until(element_present).click() # This opens the windows file selector

pyautogui.write('C://Users/user/desktop/python_project/ver2/img') 
pyautogui.press('enter')
'''


class edit_profile:
    def __init__(self, driver):
        self.driver = driver
    def edit_profile(self):
        self.driver.get('https://www.instagram.com/accounts/edit/')
        print('goto profile')
        time.sleep(2)
        change = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/article/div/div[2]/button')))
        change.click()
        print('Click change success')
        '''
        upload=WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/div[2]/button[1]')))
        upload.click()
        '''
        path = 'C:/Users/dog/desktop/ver2/img/Randoms/{random_num}.jpg'.format(random_num=str(random.randint(0,88)))

        #path = 'C:/Users/user/desktop/python_project/ver2/img/Randoms/{random_num}.jpg'.format(random_num=str(random.randint(0,88)))
        pyautogui.write(path) 
        pyautogui.press('enter')
        print('clicked enter1')

        time.sleep(5)
        pyautogui.press('enter')
        print('clicked enter2')
        time.sleep(15)
        


        