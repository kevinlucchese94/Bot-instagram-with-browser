import random
from datetime import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from ListHashtag import *
from credenziali import *

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
login_link = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
login_link.click()
sleep(10)
print(dt_string, "Ho salvato le informazioni")

for n in range(0, 3):

    for hashtag in random.choices(hashtags):
        print("hashtag", hashtag)
        browser.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        sleep(10)

        follow = browser.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]/a/div/div[2]")  # click sulla foto
        follow.click()
        sleep(10)

        for i in range(0, 10):  # per ogni hashtag segui 10 persone

            follow = browser.find_element_by_xpath(
                "/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[2]/button")  # click sul follow
            follow.click()
            sleep(10)

            follow = browser.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a[2]")  # click sulla freccia dx
            follow.click()
            sleep(10)

            print(dt_string, "Sto Seguendo", i + 1, " sull'hashtag", hashtag)

browser.close()
