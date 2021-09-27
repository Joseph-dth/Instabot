from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time
import signup
import generator
import database
import g_email


driver = 0



def main():
    global driver
    print('running auto_register.py')
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--headless')
    #chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--window-size=1980,1080")
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(chrome_options= chrome_options)
    e = g_email.g_email(driver)
    email = e.g_email()
    g = generator.generator(driver)
    user = g.generate()
    print(user)
    user[0] = email
    print(user)
    s = signup.signup(driver, user)
    
    #print(s.signup())
    if s.signup() :
        print('first step succeed')
        time.sleep(8)
        js = 'window.open("https://10minutemail.net/");'
        driver.execute_script(js)
        ig_handle = driver.current_window_handle
        handles = driver.window_handles
        print(handles)
        mail_handle = None
        for handle in handles:
            if handle !=ig_handle:
                mail_handle = handle
        print('Switch to mail')
        driver.switch_to.window(mail_handle)

        r_code = e.e_response()
        print(r_code)
        print('Switch to ig')
        driver.switch_to.window(ig_handle)
        response_type = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main > div > article > div > div:nth-child(1) > div > div.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.lC6p0 > form > div.Igw0E.IwRSH.eGOV_._4EzTm.DhRcB > input')))
        response_type.click()
        response_type.send_keys(r_code)
        but = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main > div > article > div > div:nth-child(1) > div > div.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.lC6p0 > form > div.Igw0E.IwRSH.eGOV_._4EzTm.aGBdT > button')))
        but.click()
        print('sign up succeeded')

    else:
        print('signup false')
        time.sleep(2000)
    #ai = auto_init.auto_init(driver, user)

    #ai.auto_init()
    #pd = profile_edit.edit_profile(driver)
    #pd.edit_profile()
    #up = upload_photo.upload_photo(user[2],user[3])
    #print(up.auto_init())
    d = database.insert(user)
    d.insert()

    time.sleep(2000)
    driver.close()



if __name__ == "__main__":
    main()