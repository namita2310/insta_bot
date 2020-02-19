

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import re
from time import sleep, strftime
# from random import randint
import pandas as pd

chromedriver_path = "/home/dell/geckodriver" # Change this to your own chromedriver path!
# webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
driver = webdriver.Firefox(executable_path=chromedriver_path)

driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)


username = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')
username.send_keys('pictures_do_speak')
password = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')
password.send_keys('kikalina')

button_login = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]')
button_login.click()
sleep(5)
notnow=driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
notnow.click()
sleep(5)

driver.get("https://www.instagram.com/explore/tags/programming/")
sleep(3)

img1=driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]")
img1.click()
sleep(5)
like=driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]")
like.click()
sleep(5)

for i in range(0,10):
    next_butt=driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a")
    next_butt.click()
    sleep(5)
    like=driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]")
    like.click()
    sleep(5)
