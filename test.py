from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup as b
import random
'''
name = 'zhangsan'
age = 25
price = 4500.225
info = 'my name is {my_name},i am {my_age} years old,my price is {my_price}'\
 .format(my_name=name,my_age=age,my_price=price)
print(info)

random_num = str(random.randint(0,88))
print(random_num)

path = 'C:/Users/user/desktop/python_project/ver2/img/Randoms/{random_num}.jpg'.format(random_num=str(random.randint(0,88)))
print(path)
'''

text = 'asdos'
num = '123'
text = text + num
print(text)
account_name = 'ajdll'
account_name = account_name + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
print(account_name)


chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--headless')
    #chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--window-size=1980,1080")

driver = webdriver.Chrome(chrome_options=chrome_options)
