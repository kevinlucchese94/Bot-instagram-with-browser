from datetime import datetime
from time import sleep

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from credenziali import *

options = Options()
#options.add_argument('--headless')
#options.add_argument('--disable-gpu')
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
for n in range(0, 6):  # considera il secondo numero moltiplicato per 5
    browser.get("https://www.instagram.com/" + username)
    # unfollow = browser.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[
    # 1]/div/div/div" "[2]/div[1]/div/div/a") unfollow.click()
    sleep(10)
    unfollow = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a")
    unfollow.click()
    sleep(10)
    unfollow = browser.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul/div/li[1]/div/div[3]/button")
    unfollow.click()  # click su unfollow
    sleep(3)
    if browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[1]"):
        unfollow = browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[1]")
        unfollow.click()  # click su sicurezza
        sleep(3)
    unfollow = browser.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul/div/li[2]/div/div[3]/button")
    unfollow.click()  # click su unfollow
    sleep(3)
    if browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[1]"):
        unfollow = browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[1]")
        unfollow.click()  # click su sicurezza
        sleep(3)
    unfollow = browser.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul/div/li[3]/div/div[3]/button")
    unfollow.click()  # click su unfollow
    sleep(3)
    if browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[1]"):
        unfollow = browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[1]")
        unfollow.click()  # click su sicurezz
        sleep(3)
    unfollow = browser.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul/div/li[4]/div/div[3]/button")
    unfollow.click()  # click su unfollow
    sleep(3)
    if browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[1]"):
        unfollow = browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[1]")
        unfollow.click()  # click su sicurezza
        sleep(3)
    unfollow = browser.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul/div/li[5]/div/div[3]/button")
    unfollow.click()  # click su unfollow
    sleep(3)
    if browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[1]"):
        unfollow = browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[1]")
        unfollow.click()  # click su sicurezza
        sleep(3)
    print(dt_string, "Ho eseguito l'unfollow sulle ultime", n * 5, "persone")

browser.close()
