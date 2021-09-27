from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
from selenium.webdriver.support.ui import Select
import random
import time




class signup:

    def __init__(self, driver, user):
        self.driver = driver
        self.user = user
    def signup(self):
        
        self.driver.get('https://www.instagram.com/accounts/emailsignup/?hl=zh-tw')
        try:
            email = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')))
            email.click()
            email.send_keys(self.user[0])
            time.sleep(2)
            username = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/div/label/input')))
            username.click()
            username.send_keys(self.user[1])
            time.sleep(2)
            account_name = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[5]/div/label/input')))
            account_name.click()
            account_name.send_keys(self.user[2])
            time.sleep(2)
            password = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[6]/div/label/input')))
            password.click()
            password.send_keys(self.user[3])
            time.sleep(2)
            but = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[7]/div/button')))
            but.click()
            time.sleep(5)
            s1 = Select(self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[1]/select'))
            selection = str(random.randint(1,6))
            s1.select_by_value(selection)
            time.sleep(2)
            selection = str(random.randint(1,17))
            s2 = Select(self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[2]/select'))
            s2.select_by_value(selection)
            time.sleep(2)
            s3 = Select(self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[3]/select'))
            selection = str(random.randint(1990, 2000))
            s3.select_by_value(selection)
            time.sleep(2)
            but = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[5]/div[2]/button')))
            but.click()
        except:
            email = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[1]/div/label/input')))
            email.click()
            email.send_keys(self.user[0])
            time.sleep(2)
            username = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')))
            username.click()
            username.send_keys(self.user[1])
            time.sleep(2)
            account_name = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')))
            account_name.click()
            account_name.send_keys(self.user[2])
            time.sleep(2)
            password = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/div/label/input')))
            password.click()
            password.send_keys(self.user[3])
            time.sleep(2)
            but = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[5]/div')))
            but.click()
            time.sleep(5)
            s1 = Select(self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[1]/select'))
            selection = str(random.randint(1,6))
            s1.select_by_value(selection)
            time.sleep(2)
            selection = str(random.randint(1,17))
            s2 = Select(self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[2]/select'))
            s2.select_by_value(selection)
            time.sleep(2)
            s3 = Select(self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[3]/select'))
            selection = str(random.randint(1990, 2000))
            s3.select_by_value(selection)
            time.sleep(2)
            but = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[5]/div[2]/button')))
            but.click()
        '''
        try:
            time.sleep(5)
            btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main > div > div > div > div > button')))
            btn.click()
            #btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')))
            #btn.click()
        except:
            print('click adds false')
            return False
        '''
        return True

  