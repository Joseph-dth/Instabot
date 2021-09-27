from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time

class Getpages:
    def __init__(self,driver):
        self.driver = driver
        #self.driver.get('https://www.instagram.com/snowbabyq/')
        self.driver.get('https://www.instagram.com/deyn_li/')
        self.hrefs = []

    def get_num_flw(self):
        flw = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main')))
        sflw = b(flw.get_attribute('innerHTML'), 'html.parser')
        #print(sflw)
        followers = sflw.findAll('span', {'class':'g47SY'})
        f = followers[1].getText()
        if '萬' in f:
            f=float(f[:-1])*10**4
        else:
            f=float(f)
        print(f)
        return f 
       
    def get_followers(self):
        time.sleep(2)
        print('getting followers')
        flwr_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main > div > header > section > ul > li:nth-child(2) > a')))
        flwr_btn.click()
        print('Click followes success')
        self.popup = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]')))
        for h in range(11):
            print('scrolling', h)
            time.sleep(2)
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight/{}'.format(str(11-h)), self.popup)#scroll with javascript
        for h in range(5):
            print('scrolling', h)
            time.sleep(2)
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', self.popup)#scroll with javascript
        self.popup = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]')))
        b_popup = b(self.popup.get_attribute('innerHTML'), 'html.parser')
        print(b_popup.prettify())
        ap=b_popup.find_all('li', {'class':'wo9IH'})
        #print(ap)
        #print('----------')
        #print(ap.prettify())
        for p in ap:
            #print(p)
            try:
                #hlink = p.find('a').string
                hlink = p.find_all('a')[0].get('href')

                #print(hlink)
                '''
                if 'div' in hlink:
                    return self.hrefs
                else:
                    self.hrefs.append(hlink)
                '''
                self.hrefs.append(hlink)

            except:
                print('Get followes false')
            #print(p.find_All('a')[0]['href'])
        return self.hrefs
        #self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', self.popup)#scroll with javascript

        # 12 followers/ loading

    def is_public(self):
        #account
        try:
            astate = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'rkEop')))
            if astate.text == '此帳號為私人帳號':
                return False
            else:
                return True
        except:
            return True
            # Most likely a public account i guess lol

    def like_post(self):
        post =self.driver.find_element_by_css_selector('#react-root > section > main > div > div._2z6nI > article > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(1) > a')
        html = post.get_attribute('innerHTML')
        h = b(html, 'html.parser')
        #print(h)
        href = h.find_all('a')[0].get('href')
        print(href)

        self.driver.get('https://www.instagram.com'+href)
        like_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.FY9nT.fr66n > button')))
        like_btn.click()

    def follow_page(self):
        follow = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/div[1]/button')))
        f_text = follow.text
        if f_text == '追蹤' or f_text == '追蹤對方' :
            follow.click()
        elif f_text =='已送出請求' or f_text =='追蹤中' or f_text =='發送訊息':
            print('Already follow')
        time.sleep(1)