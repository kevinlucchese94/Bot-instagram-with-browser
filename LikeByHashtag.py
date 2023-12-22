import random
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ListHashtag import *
from credenziali import *

options = webdriver.FirefoxOptions()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
browser = webdriver.Firefox(options=options)
wait = WebDriverWait(browser, 10)

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

browser.get('https://www.instagram.com/')

try:
    cookie_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/button[1]")))
    cookie_btn.click()
    print(dt_string, "Ho accettato i cookies")
except Exception as e:
    print(dt_string, "Pulsante dei cookies non trovato o già accettato.")


# Inserisci Username e Password
username_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='username']")))
password_input = browser.find_element_by_css_selector("input[name='password']")
username_input.send_keys(username)
password_input.send_keys(password)

login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]")))
login_btn.click()
print(dt_string, "Ho eseguito l'accesso")

# Salva le informazioni
save_info_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/main/div/div/div/div/button")))
save_info_btn.click()

for n in range(0, 3):
    for hashtag in random.choices(hashtags):
        print("hashtag", hashtag)
        browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
        sleep(10)import random
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ListHashtag import *
from credenziali import *

options = webdriver.FirefoxOptions()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
browser = webdriver.Firefox(options=options)
wait = WebDriverWait(browser, 10)

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

browser.get('https://www.instagram.com/')

# Accetta i cookies
cookie_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='_g8n0']")))
cookie_btn.click()
print(dt_string, "Ho accettato i cookies")

# Inserisci Username e Password
username_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id='username']")))
password_input = browser.find_element_by_css_selector("input[id='password']")
username_input.send_keys(username)
password_input.send_keys(password)

login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
login_btn.click()
print(dt_string, "Ho eseguito l'accesso")

# Salva le informazioni
save_info_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Salva le informazioni']")))
save_info_btn.click()

for n in range(0, 3):
    for hashtag in random.choices(hashtags):
        print("hashtag", hashtag)
        browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
        sleep(10)

        # Clicca sulla prima immagine
        image_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='_7UhW9']")))
        image = image_element.find_element_by_tag_name('img')
        image.click()
        sleep(10)

        for i in range(0, 10):
            like_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Mi piace']")))
            like_btn.click()
            sleep(10)

            next_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='coreSpriteRightArrow']")))
            next_btn.click()
            sleep(10)

            print(dt_string, f"Ho messo {i + 1} Like sull'hashtag {hashtag}")

browser.quit()


        # Clicca sulla prima immagine
        image = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.v1Nh3")))
        image.click()
        sleep(10)

        for i in range(0, 10):
            like_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".fr66n")))
            like_btn.click()
            sleep(10)

            next_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div[1]/div/div/a[2]")))
            next_btn.click()
            sleep(10)

            print(dt_string, f"Ho messo {i + 1} Like sull'hashtag {hashtag}")

browser.quit()
