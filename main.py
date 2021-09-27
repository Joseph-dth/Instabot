from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time
import login
import getpages

username = 'alexander_in_m'
password = 'awp038500'

driver = 0
refs = []
max_likes = 50
max_follows = 20 

def main():
    global driver
    print('running scripts...')

    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--headless')
    #chrome_options.add_argument('--no-sandbox')
    #chrome_options.add_argument("--window-size=900,780")

    driver = webdriver.Chrome(chrome_options=chrome_options)
    #driver = webdriver.Chrome()
    l = login.Login(driver, username, password)
    l.signin()
    gp = getpages.Getpages(driver)
    refs = gp.get_followers()
    print(refs)
    
    gp.get_num_flw()
    run_bot(refs, driver, gp)

def run_bot(refs, driver, gp):
    t = time.time()
    #Ammounts of likes
    Likes = 0
    #Ammounts of Follows
    Follows = 0

    for r in refs:
        driver.get('https://www.instagram.com' + r)
        time.sleep(2)
        if gp.get_num_flw() < 3000:
            if gp.is_public():
                print('public account')
                print('current likes' + str(Likes))
                '''
                if Likes < max_likes:
                    time.sleep(2)
                    gp.like_post()
                    Likes +=1
                    print('POST LIKED') 
                else:
                    time.sleep(3600)
                    print('sleeping')
                '''
                print('current follows:'+str(Follows))
                if Follows < max_follows:
                    time.sleep(2)
                    gp.follow_page()
                    print('page followed successfully')
                    Follows +=1
                else:
                    time.sleep(3600)
                    print('sleeping')
            else:
                print('private account')
                print('current follows:'+str(Follows))
                if Follows < max_follows:
                    time.sleep(2)
                    gp.follow_page()
                    print('page followed successfully')
                    Follows +=1
                else:
                    time.sleep(3600)
                    print('sleeping')

if __name__== '__main__':
    main()