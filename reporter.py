from time import sleep
import keyboard as kb
import json
import undetected_chromedriver as uc

import os
import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService

# Function to load the configuration
def load_config():
    with open('config.json', 'r') as config_file:
        return json.load(config_file)

# Function to initialize the WebDriver
def init_driver():
    options = Options()
    options.page_load_strategy = 'eager'
    options.headless = False
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("--log-level=OFF")
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(options=options)
    return driver

# Function to login to Instagram
def login_instagram(driver, username, password):
    wait = WebDriverWait(driver, 100)
    driver.get(f'https://www.instagram.com/accounts/login/')
    
    cookies = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Only allow essential cookies']")))
    cookies.click()

    username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))

    username_field.clear()
    username_field.send_keys(username)
    
    password_field.clear()
    password_field.send_keys(password)

    login_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
    login_button.click()

    save_login_info = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Save Info']")))
    save_login_info.click()

# Function to report a user
def report_user(driver, username_report):
    wait = WebDriverWait(driver, 100)
    driver.get(f'https://www.instagram.com/{username_report}/')

    while True:
        more = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='More options']")))
        more.click()

        report = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Report User']")))
        report.click()

        report_acc = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Report Account']")))
        report_acc.click()

        second = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Report']")))
        second.click()

        me = wait.until(EC.presence_of_element_located((By.XPATH, "//label[text()='It’s inappropriate']")))
        me.click()

        submit = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Submit Report']")))
        submit.click()

        close = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Close']")))
        close.click()

# Main execution
if __name__ == "__main__":
    os.system('cls & title Instagram Reporter ~ unofficialdxnny')

    data = load_config()
    username_report = input("Username to report > ")

    driver = init_driver()
    print('Logging into Instagram')

    login_instagram(driver, data["username"], data["password"])
    report_user(driver, username_report)
