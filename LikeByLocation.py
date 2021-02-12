from time import sleep
from datetime import datetime
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import random
from credenziali import *
from ListLocation import *

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
browser = webdriver.Firefox(options=options)
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

browser.get('https://www.instagram.com/')

login_link = browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]")  # accetta i cookies
sleep(10)
login_link.click()
print(dt_string, "Ho accettato i cookies")
print(dt_string, "Inserisco Username e pwd")
username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")

username_input.send_keys(username)
password_input.send_keys(password)

login_link = browser.find_element_by_xpath(
    "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]")  # click su login
login_link.click()
sleep(10)
print(dt_string, "Ho eseguito l'accesso")
login_link = browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
login_link.click()
sleep(10)
print(dt_string, "Ho salvato le informazioni")

for hashtag in random.choices(location):  # fa il giro di tutti gli hashtag impostati

    for i in range(0, 5):  # per ogni hashtag metti 3 like
        browser.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        sleep(10)

        like = browser.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]/a/div/div[2]")  # click sulla foto
        like.click()
        sleep(10)

        actions = ActionChains(browser)
        actions.send_keys(Keys.TAB * 5)
        actions.send_keys(Keys.SPACE)
        actions.perform()
        sleep(10)

        print(dt_string, "Ho messo", i + 1, "Like sull'hashtag", hashtag)

browser.close()
