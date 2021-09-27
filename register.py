from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time
import signup
import generator


driver = 0



def main():
    print('running register.py')
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--headless')
    #chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--window-size=1980,1080")
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(chrome_options= chrome_options)
    g = generator.generator(driver)
    user = g.generate()
    print(user)
    s = signup.signup(driver, user)
    print(s.signup())
    time.sleep(180)

if __name__ == "__main__":
    main()